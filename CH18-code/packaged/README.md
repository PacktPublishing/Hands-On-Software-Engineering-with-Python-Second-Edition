# The `packaged` directory

This directory may contain a locally-packaged copy of the Lambda Function code in the `src`
directory for the project, created with the project's `packaging` tool script (see the
`[scripts]` section of [the project's `Pipfile`](../Pipfile)).

The base command is:

```shell
pipenv run packaging
```

...and it has help information available:

```
usage: package-lambdas [-h] {clean,lambdas} ...

A developer tool that creates Lambda Function packages (ZIP files) from the project structure.

positional arguments:
  {clean,lambdas}  Commands
    clean          Remove all packages from the packaged directory
    lambdas        Create packages for all or some Lambda Function directories under the src directory.

options:
  -h, --help       show this help message and exit
```

## `pipenv run packaging lambdas --help`

```
usage: package-lambdas lambdas [-h] [--targets [TARGETS ...]] [--include-common]

options:
  -h, --help            show this help message and exit
  --targets [TARGETS ...], -t [TARGETS ...]
                        The Lambda Function directories to package. Directories MUST have a matching category entry
                        in the CH18-code/src directory! If not specified, ALL directory/category items will be
                        processed.
  --include-common, -i  Whether to include the code in the "common" directory in the package(s). If not included,
                        that code will NOT be included.
```
