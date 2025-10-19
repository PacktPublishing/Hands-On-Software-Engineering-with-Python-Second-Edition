#!/usr/bin/env python3
"""
Script to create the HMS Core package project structure.
Run this script to automatically generate all files and directories.
"""

import os
import sys

# File contents
FILE_CONTENTS = {
    'Makefile': """.PHONY: clean lint test test-unit test-integration test-system coverage build publish

# Python settings
PYTHON = python
PIP = pip
PIPENV = pipenv

# Project settings
PROJECT_NAME = hms-core
SRC_DIR = src
TEST_DIR = tests

# Clean build artifacts
clean:
\t@echo "Cleaning build artifacts..."
\trm -rf build/
\trm -rf dist/
\trm -rf *.egg-info
\tfind . -type d -name __pycache__ -exec rm -rf {} +
\tfind . -type f -name "*.pyc" -delete
\tfind . -type f -name "*.pyo" -delete
\tfind . -type f -name "*.pyd" -delete
\tfind . -type f -name ".coverage" -delete
\tfind . -type d -name "*.egg" -exec rm -rf {} +
\tfind . -type d -name "*.eggs" -exec rm -rf {} +
\tfind . -type d -name "*.pytest_cache" -exec rm -rf {} +
\tfind . -type d -name "htmlcov" -exec rm -rf {} +
\t@echo "Clean complete!"

# Install dependencies
install:
\t$(PIPENV) install --dev

# Lint code
lint:
\t@echo "Linting code..."
\t$(PIPENV) run flake8 $(SRC_DIR)
\t@echo "Lint complete!"

# Run unit tests
test-unit:
\t@echo "Running unit tests..."
\t$(PIPENV) run pytest $(TEST_DIR)/unit -v
\t@echo "Unit tests complete!"

# Run integration tests
test-integration:
\t@echo "Running integration tests..."
\t$(PIPENV) run pytest $(TEST_DIR)/integration -v
\t@echo "Integration tests complete!"

# Run system tests
test-system:
\t@echo "Running system tests..."
\t$(PIPENV) run pytest $(TEST_DIR)/system -v
\t@echo "System tests complete!"

# Run all tests
test: test-unit test-integration test-system
\t@echo "All tests complete!"

# Generate coverage report
coverage:
\t@echo "Generating coverage report..."
\t$(PIPENV) run coverage run -m pytest $(TEST_DIR)
\t$(PIPENV) run coverage report -m
\t$(PIPENV) run coverage html
\t@echo "Coverage report complete!"

# Build package
build: clean lint test
\t@echo "Building package..."
\t$(PIPENV) run python -m build
\t@echo "Build complete!"

# Publish package
publish: build
\t@echo "Publishing package..."
\t$(PIPENV) run twine check dist/*
\t$(PIPENV) run twine upload dist/*
\t@echo "Publish complete!"

# Default target
all: clean lint test build
""",

    'Pipfile': """[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
# Add your production dependencies here

[dev-packages]
pytest = "<9.0.0"
flake8 = "<7.0.0"
coverage = "<8.0.0"

[build]
build = "<1.0.0"

[publish]
twine = "<5.0.0"

[requires]
python_version = "3.9"
""",

    'README.md': """# HMS Core Package

## Overview
This package provides core functionality for the HMS namespace.

## Installation
To install the package for development:

```bash
# Install pipenv if not already installed
pip install pipenv

# Install dependencies
pipenv install --dev
```

## Project Structure
```
.
├── Makefile               # Contains build and test automation
├── Pipfile                # Pipenv dependencies
├── README.md              # This file
├── pyproject.toml         # Package metadata and build configuration
├── src                    # Source code
│   └── hms
│       ├── __init__.py
│       └── core
│           └── __init__.py
└── tests                  # Test suites
    ├── integration        # Integration tests
    ├── system             # System tests
    └── unit               # Unit tests
```

## Development

### Running Tests
```bash
# Run all tests
make test

# Run only unit tests
make test-unit

# Run only integration tests
make test-integration

# Run only system tests
make test-system
```

### Linting
```bash
make lint
```

### Coverage Report
```bash
make coverage
```

### Building Package
```bash
make build
```

### Publishing Package
```bash
make publish
```

## License
MIT
""",

    'pyproject.toml': """[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "hms-core"
version = "0.1.0"
description = "HMS Core Package"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    # Add your dependencies here
]

[project.urls]
"Homepage" = "https://github.com/yourusername/hms-core"
"Bug Tracker" = "https://github.com/yourusername/hms-core/issues"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
namespace_packages = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
""",

    'src/hms/__init__.py': """\"\"\"HMS package namespace.\"\"\"

__import__('pkg_resources').declare_namespace(__name__)
""",

    'src/hms/core/__init__.py': """\"\"\"HMS Core package.\"\"\"

__version__ = '0.1.0'
""",

    'tests/unit/test_hms/test_core/__init__.py': """\"\"\"Unit tests for the HMS Core package.\"\"\"
""",

    'tests/integration/test_hms/test_core/__init__.py': """\"\"\"Integration tests for the HMS Core package.\"\"\"
""",

    'tests/system/test_hms/test_core/__init__.py': """\"\"\"System tests for the HMS Core package.\"\"\"
""",

    'tests/unit/test_hms/test_core/test_example.py': """\"\"\"Example unit test for the HMS Core package.\"\"\"

import pytest
from hms.core import __version__


def test_version():
    \"\"\"Test that the version string is valid.\"\"\"
    assert __version__ == '0.1.0'
"""
}

# Directory structure
DIRECTORIES = [
    'src/hms/core',
    'tests/unit/test_hms/test_core',
    'tests/integration/test_hms/test_core',
    'tests/system/test_hms/test_core'
]

def create_directories(root_dir):
    """Create the directory structure."""
    for directory in DIRECTORIES:
        os.makedirs(os.path.join(root_dir, directory), exist_ok=True)

def create_files(root_dir):
    """Create all files with their content."""
    for filepath, content in FILE_CONTENTS.items():
        full_path = os.path.join(root_dir, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, 'w') as f:
            f.write(content)

def main():
    """Create the project structure."""
    root_dir = 'hms-core-project'

    # Create the root directory
    os.makedirs(root_dir, exist_ok=True)

    # Create the directory structure
    create_directories(root_dir)

    # Create all files
    create_files(root_dir)

    print(f"Project structure created in '{root_dir}' directory.")
    print("You can now use your own tools to ZIP this directory.")

if __name__ == '__main__':
    main()
