# Project Creation: PyCharm and `pipenv`

- Create the project folder with PyCharm’s *New Project…* menu-command, using a `pipenv` environment.
  
  - This created the initial `Pipfile`

- Using PyCharm's *Terminal*:
  
  - Install the development-only package dependencies with
    
    ```bash
    pipenv install --dev flake8 pytest
    ```
  
  - Install the project’s required package dependency with
    
    ```bash
    pipenv install requests
    ```
  
  **Note:** When a PyCharm project is set up with `pipenv`, its *Terminal* launches inside the project’s PVE. This raises the following Courtesy Notice when any `pipenv` command is executed therein:
  
  > Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project.

- Additional project-level configuration items:
  - `Project --> Settings --> Project: (project name) --> Project Structure` may be needed to identify *Sources* directories so that other modules can import from the project
  - Setting a default Run/Debug configuration for Python files, so that any Python file will run with the *Current File* selected, at `Run --> Edit Configurations… --> Edit Configuration Templates --> Python`:
    - Set the working directory to the project root
    - Enable EnvFile and point to the project's `.env` file
    - Add source roots to `PYTHONPATH`

- Create the project's directory-structure and add the `main.py` and `test_main.py` modules, and the `.env` file in the appropriate locations

- Run the added modules
  - PyCharm's *Run* command apparently doesn't go through the PVE created, so it won't recognize the `.env` file, though running a module from the integrated terminal works as expected.
  - When the `.env` file was opened, an info-banner was presented offering to install a plug-in to support `.env` files. Those work, but require additional configuration.
  - Setting the `PYTHONPATH` environment-variable in the `Project --> Settings --> Build, Execution, Deployment --> Console --> Python Console` configuration did *not* behave as expected, but with one of the `.env`-file plug-ins in place, and configured, that issue was resolved.
  - PyCharm auto-recognizes test modules and methods, and won't allow them to be run as anything but a test-module without creating a custom configuration.

---

> **Note:** PyCharm didn't recognize Python 3.11, so the `pyenv` hook provided by `pipenv` offered to install it. After that installation, I had to restart PyCharm for the environment to be recognized.
> 
> I also found that I had to configure the new project to point to the `pipenv` PVE. Finding the pathto the interpreter was not difficult:
> 
> ```bash
> pipenv run which python
> ```