- Create project directory (`vscode-examples/pipenv/example_project`) using the *File* --> *Open Folder…* menu-command
- Create the project's directory-structure
- Create the `pipenv` PVE with 
  ```bash
  pipenv --python {path-to-python|python-version-number}
  ```
  **Note:** this will show the path to the created PVE. Keep track of that, since it will be needed later!
- Create the first Python module at `src/example_project/main.py`
- Click the *Select Interpreter* prompt (lower right)
  - Click *Create Virtual Environment…*
  - If the PVE is in the list, select it, otherwise click *Enter interpreter path…* and use the path from `pipenv --venv` as a starting-point to select the `Python3.XX` executable.
- Kill any already-running *Python* terminals
- Create the project files