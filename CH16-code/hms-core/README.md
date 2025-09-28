# The `hms-code` Python Package

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
pipenv sync
```

- Make a copy of the `template.env` file, naming it `.env`,
  and populate any items indicated

