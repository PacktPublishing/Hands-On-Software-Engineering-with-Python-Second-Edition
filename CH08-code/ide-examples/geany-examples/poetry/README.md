# Example Project with pipenv (Geany)

The process for creating this project, using pipenv to manage package dependencies and the related PVE, step-by-step:

```bash
cd {project-parent-directory}
poetry new example_project 
```

At this point, the project directory looks like this, because `poetry` creates the project structure along with the support files needed to build a package:

```
├── example_project
│   └── __init__.py
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py
```

Create the Geany project with Geany's `Project` --> `New…` command. Because the PVE is managed with `poetry`, it looks for the `pyproject.toml` file that was created, which lives next to the package-root directory (the `example_project` directory that contains the created `__init__.py` module), the project's base path needs to point to the directory where that file lives.

> These were run in the Terminal tab of the Message Window, but could be executed in ANY terminal, so long as they are executed in the directory where the `pyproject.toml` file lives.

```bash
poetry add --group=dev flake8 pytest  # Common development-only packages
```

Open any Python module file (I used `example_project/__init__.py`) so Geany will recognize that Python configuration should be available, then open it in the editor.

Under the Build menu --> Set Build Commands:

- Click the "Lint" button to change its name to Lint Python Module, and change its command to `cd "%p";poetry run flake8 "%d/%f"`
- Change the command for the Execute button to `cd "%p";poetry run python "%d/%f"`

`poetry` does not have a single, clear mechanism for handling environment variables that does not involve adding them to the command-line invocation in the Execute configuration.

To get around that, this variant of the project also includes the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package:

```bash
poetry add python-dotenv
```

This allows the same `.env` file structure to be used as is in place in the `pipenv` example:

```
PACKAGE_MANAGER="poetry"
IDE="Geany"
```

Write the code in `main.py`. In order to show the use of a third-party package, it imports `requests`, which needs to be installed with

```bash
poetry add requests
```

Create the first unit-test module at `tests/test_main.py`

At this point, the bare-bones project structure is complete. The `main.py` module can be run within Geany by pressing the F5 key while that module is active in the editor window. So too can the test-module if *it* is active:

```
Running .../poetry/example_project/example_project/main.py
Example using poetry in Geany
The requests module: 
    <module 'requests' 
    from '.../pypoetry/virtualenvs/{PVE}/.../site-packages/requests/__init__.py'>

A bare-bones project module. All this module does is print that
it's being run, this docstring, and the interpreter that it's
running under.

Project Python interpreter: .../pypoetry/virtualenvs/{PVE}/bin/python


------------------
(program exited with code: 0)
Press return to continue
```

```
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-8.2.1, pluggy-1.5.0 -- 
   .../pypoetry/virtualenvs/{PVE}/bin/python
cachedir: .pytest_cache
rootdir: .../poetry/example_project
configfile: pyproject.toml
collected 1 item                                                               

tests/test_main.py::test_nothing PASSED                                  [100%]

============================== 1 passed in 0.01s ===============================
```
