# Example Project with pipenv (Geany)

The process for creating this project, using pipenv to manage package dependencies and the related PVE, step-by-step:

Manual creation of a project directory is not needed in this case: Geany's `Project` --> `New…` command allows the user to create the project's root directory in the IDE itself. If there's a need or desire to create it manually for some reason, this would suffice:

```bash
mkdir example_project 
```

> These were run in the Terminal tab of the Message Window, but could be executed in ANY terminal

```bash
cd example_project                  # Navigate to the project directory
touch Pipfile                       # Making sure that the Pipfile exists first
pipenv --python 3.11                # Using Python 3.11 in the PVE
pipenv install --dev flake8 pytest  # Common development-only packages
```

> A simple bash command to create a typical project-directory structure.

```bash
mkdir -p src/example_project tests/unit/test_example_project
```

At this point, the project directory looks like this

```
├── Pipfile
├── Pipfile.lock
├── src
│   └── example_project
└── tests
    └── unit
        └── test_example_project
```

Create any Python module file (I used `src/example_project/main.py`, since it would be created later otherwise) so Geany will recognize that Python configuration should be available, then open it in the editor.

Under the Build menu --> Set Build Commands:

- Click the "Lint" button to change its name to Lint Python Module, and change its command to `cd "%p";pipenv run flake8 "%d/%f"`
- Change the comamnd for the Execute button to `cd "%p";pipenv run python "%d/%f"`

Create a `.env` file, and populate it with:

```
PACKAGE_MANAGER="pipenv"
IDE="Geany"
```

Write the code in `main.py`. In order to show the use of a third-party package, it imports `requests`, which needs to be installed with

```bash
pipenv install requests
```

Create the first unit-test module at `tests/unit/test_example_project/test_main.py`

At this point, the bare-bones project structure is complete. The `main.py` module can be run within Geany by pressing the F5 key while that module is active in the editor window. So too can the test-module if *it* is active:

```
Loading .env environment variables...
Running .../ide-examples/geany-examples/pipenv/example_project/src/example_project/main.py
Example using pipenv in Geany
The requests module: <module 'requests' from '.../{PVE}/lib/python3.11/site-packages/requests/__init__.py'>

A bare-bones project module. All this module does is print that
it's being run, this docstring, and the interpreter that it's
running under.

Project Python interpreter: .../{PVE}/bin/python


------------------
(program exited with code: 0)
Press return to continue
```

```
Loading .env environment variables...
============================= test session starts ==============================
platform linux -- Python 3.11.0rc1, pytest-8.2.1, pluggy-1.5.0 -- .../{PVE}/bin/python
cachedir: .pytest_cache
rootdir: .../ide-examples/geany-examples/pipenv/example_project
collected 1 item                                                               

tests/unit/test_example_project/test_main.py::test_nothing PASSED        [100%]

============================== 1 passed in 0.01s ===============================


------------------
(program exited with code: 0)
Press return to continue

```
