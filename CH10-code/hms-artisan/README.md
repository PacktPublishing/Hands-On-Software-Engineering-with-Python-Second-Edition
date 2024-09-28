# The `hms-artisan` Python Package

This README file would include whatever the owners of the
code feels would be relevant or useful to consumers of the
package, or to developers who are going to make changes to
it.

Common sections might include:

- Installation instructions

- How-Tos -- examples of using the package once it's been
  installed

## Setting up for development

**Prerequisites:**

- A working installation of [pipenv](https://pipenv.pypa.io/en/latest/),
  version `2023.12.1` or later.

### Initial set-up

When first cloning the project repo, you will need to set up
the project's Python Virtual Environment (PVE):

- Navigate to the project root directory (where the [Pipfile](Pipfile) lives).

- Execute the following commands (some versions of `pipenv`
  do not sync everything with a `pipenv sync`, just to be
  safe, run them all:
  ```shell
  pipenv sync --dev
  pipenv sync --categories build_publish
  pipenv sync
  ```

- Make a copy of the `template.env` file, naming it `.env`,
  and populate any items indicated

- Consider using the [project hooks](hooks/README.md).

### Post-checkout set-up

If you already have a local copy of the code base, here are
some recommended actions you should consider at various points
in your work.

If you haven't configured the [project hooks](hooks/README.md),
manually do what they do:

- After a checkout or merge (pull):
  - Run `pipenv update` to fetch and install any updates for
    package dependencies.
  - Run the [security-scans script](hook-scripts/security-scans.py)
    to check for known vulnerabilities, and investigate any
    that surface.
- Before pushing your work:
  - Run the [security-scans script](hook-scripts/security-scans.py)
    to check for known vulnerabilities, and investigate any
    that surface.
  - Run the unit test suite:
    ```shell
    pipenv run pytest tests/unit
    ```
  - Lint the source and test code:
    ```shell
    pipenv run flake8 src
    pipenv run flake8 tests
    ```
