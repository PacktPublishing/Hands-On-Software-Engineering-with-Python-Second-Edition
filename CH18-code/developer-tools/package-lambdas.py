#!/usr/bin/env python3.11
"""
A developer tool that creates Lambda Function packages (ZIP files) from the project structure.
"""

# Built-In Imports
import argparse
import os
import sys

from datetime import datetime
from functools import cache
from pathlib import Path
from shutil import copy, copy2, copytree, which, rmtree
from subprocess import run, CalledProcessError
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_DEFLATED

# Third-Party Imports
import boto3
import toml

# Module "Constants" and Other Attributes
EPILOG = """"""

PROJECT_ROOT = Path(__file__).parent.parent
pipfile = PROJECT_ROOT / 'Pipfile'
packaged_dir = PROJECT_ROOT / 'packaged'
src_dir = PROJECT_ROOT / 'src'
common_dir = PROJECT_ROOT / 'common'
pip = which('pip')


@cache
def __get_targets() -> list[str]:
    """
    Returns a list of viable targets for packaging.

    The list is the common names between the project's
    Pipfile and the directory names under the src_dir
    directory.
    """
    pipfile_data = toml.loads(pipfile.read_text())
    pipfile_names = [
        item for item in pipfile_data.keys()
        if (src_dir / item).exists()
    ]
    return pipfile_names


def copy_contents(src: Path, dst: Path) -> None:
    """
    Recursively copy all files and subdirectories from src into dst.

    - src and dst must both be directories.
    - Creates dst if it does not exist.
    - Existing files in dst are overwritten.
    """
    if not src.is_dir():
        raise ValueError(f'Source {src} is not a directory')

    dst.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            # Recursively copy subdirectory
            copytree(item, target, dirs_exist_ok=True)
        else:
            copy2(item, target)



def __clean__(*args, **kwargs):
    """
    """
    print('__clean__ called:')
    print(f'args ..... {args}')
    print(f'kwargs ... {kwargs}')
    print(f'Project root ..... {PROJECT_ROOT.name}')
    for item in packaged_dir.iterdir():
        if item.is_dir():
            rmtree(item)
        if item.name.endswith('zip'):
            item.unlink()


def _get_or_create_target_dir(target_dir: Path):
    if not target_dir.exists():
        target_dir.mkdir()
    if not target_dir.is_dir():
        raise RuntimeError(
            f'target_dir {target_dir} already exists, '
            'and is not a directory'
        )
    return target_dir


def _copy_source_code(target, tmp_src, tempdir, include_common):
    print('- Copying files')
    copy_contents(tmp_src, tempdir)
    categories = [target]
    if include_common:
        print(f'- Copying files from {common_dir.name}')
        categories.append(common_dir.name)
    return categories


def _generate_requirements_file(target, categories, reqs_file):
        print(
            f'- Generating {target} requirements.txt at '
            f'{reqs_file.relative_to(PROJECT_ROOT)}'
        )
        cmd = (
            f'pipenv requirements --categories '
            f'"{", ".join(categories)}" > '
            f'"{reqs_file.resolve()}"'
        )
        try:
            result = run(cmd, shell=True, capture_output=True)
        except CalledProcessError as error:
            print(f'Command {cmd} failed. Results were:')
            print(error.stderr)


def _install_target_requirements(reqs_file):
    print(
        '- Installing packages from '
        f'{reqs_file.relative_to(PROJECT_ROOT)} into '
        f'{reqs_file.parent.relative_to(PROJECT_ROOT)}.'
    )
    cmd = (
        f'{pip} install -r "{reqs_file}" '
        f'--target "{reqs_file.parent}"'
    )
    try:
        result = run(cmd, shell=True, capture_output=True)
    except CalledProcessError as error:
        print(f'Command {cmd} failed. Results were:')
        print(error.stderr)


def _package_code_into_zip(package_dir, target):
    zip_file_path = packaged_dir / f'{target}.zip'
    tempdir = package_dir / target
    with ZipFile(
        zip_file_path.resolve(), mode='w',
        compression=ZIP_DEFLATED
    ) as zip_file:
        print(
            f'- Zipping {package_dir.name}{os.sep}'
            f'{tempdir.name}{os.sep}* into '
            f'{packaged_dir.name}{os.sep}'
            f'{zip_file_path.name}'
        )
        for root, dirs, files in os.walk(tempdir):
            for file_name in files:
                file_path = os.path.join(
                    root, file_name
                )
                zip_name = os.path.relpath(
                    file_path, tempdir
                )
                zip_file.write(file_path, zip_name)
    return zip_file_path


def _upload_packages_to_s3(s3_bucket, *package_files):
    print(f'- Uploading to {s3_bucket}.')
    s3 = boto3.client('s3')
    for item in package_files:
        try:
            s3.upload_file(item, s3_bucket, item.name)
            print(f' - {item.name} uploaded')
        except Exception as error:
            print(
                f' - {item.name} upload failed: '
                f'{error.__class__.__name__}: '
                f'{error}'
            )

def __main__(
    targets: list[str] = [],
    include_common: bool = False,
    s3_bucket: str | None = None,
    *args, **kwargs
):
    """
    Packages one or more Lambdas from the project's src
    directory, allowing the inclusion of common code, and
    optionally uploading the generated package-files to a
    specified AWS S3 bucket. If no Lambda targets are
    specified, ALL of them will be packaged.

    Parameters:
    -----------
    targets : list[str]
        The names of the Lambda directories (src/*) whose
        code will be packaged, one package archive per
        target name.
    include_common : bool
        Flag that triggers the inclusion of the code and
        package-dependencies from the common directory in
        the packages created.
    s3_bucket : str | None
        The name of an S3 bucket to upload the resulting
        package-files to.
    """
    print(f'Project root ..... {PROJECT_ROOT.name}')
    print(f'src_dir .......... {src_dir.relative_to(PROJECT_ROOT)}')
    if not targets:
        targets = __get_targets()
    print(f'targets .......... {targets}')
    print(f'include_common ... {include_common}')
    for target in targets:
        print(f'=== Packaging {target} '.ljust(80, '='))
        tempdir = _get_or_create_target_dir(
            packaged_dir / target
        )
        tmp_src = _get_or_create_target_dir(src_dir / target)
        print(f'- Packaging from ... {tmp_src.relative_to(PROJECT_ROOT)}')
        print(f'- Packaging into ... {tempdir.relative_to(PROJECT_ROOT)}')

        # Copy source and common code into temp dir
        categories = _copy_source_code(
            target, tmp_src, tempdir, include_common
        )

        # Generate the collective requirements for
        # the target
        tempdir_reqs = tempdir / 'requirements.txt'
        _generate_requirements_file(
            target, categories, tempdir_reqs
        )

        # Install the requirements collected above
        # in the temporary directory
        _install_target_requirements(tempdir_reqs)

        # Package the results into a ZIP file
        zip_file_path = _package_code_into_zip(
            packaged_dir, target
        )

        # Clean up the temporary directory
        print(
            f'- Removing {packaged_dir.name}{os.sep}'
            f'{tempdir.name}'
        )
        rmtree(tempdir)

        # Make a date/time-stamped copy of the package
        build_timestamp = datetime.now() \
            .strftime("%Y%m%d-%H%M%S")
        date_name = f'{target}-{build_timestamp}.zip'
        timestamped_path = packaged_dir / date_name
        print(
            '- Making a "timestamped" copy of the package file at '
            f'{timestamped_path.relative_to(PROJECT_ROOT)}.'
        )
        copy(zip_file_path, timestamped_path)

        # Upload to S3 if a bucket was provided.
        if s3_bucket:
            _upload_packages_to_s3(
                s3_bucket,
                zip_file_path, timestamped_path
            )


# Argument Parser
parser = argparse.ArgumentParser(
    prog='packaging',
    description = __doc__,
    epilog=EPILOG
)
commands = parser.add_subparsers(help='Commands')

clean = commands.add_parser(
    'clean',
    help='Remove all packages from the '
    f'{packaged_dir.name} directory'
)
clean.set_defaults(func=__clean__)

main = commands.add_parser(
    'lambdas',
    help='Create packages for all or some Lambda '
    f'Function directories under the {src_dir.name} '
    'directory.'
)
main.set_defaults(func=__main__)
main.add_argument(
    '--targets', '-t', type=str, nargs='*',
    help='The Lambda Function directories to package. '
    'Directories MUST have a matching category entry in '
    f'the project\'s Pipfile! If not specified, ALL '
    'directory/category items will be processed.'
)
main.add_argument(
    '--s3-bucket', '-b', type=str,
    help='The name of the AWS S3 bucket to upload '
    'packages to.'
)
main.add_argument(
    '--include-common', '-i', action='store_true',
    help='Whether to include the code in the '
    f'"{common_dir.name}" directory in the package(s). '
    'If not set, that code will NOT be included.'
)


if __name__ == '__main__':
    st_dir = os.getcwd()
    os.chdir(PROJECT_ROOT)
    args = parser.parse_args()
    func = args.func
    func_args = vars(args)
    del func_args['func']
    func(**func_args)
