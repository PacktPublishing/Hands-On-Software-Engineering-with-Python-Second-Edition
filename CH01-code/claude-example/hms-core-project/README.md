# HMS Core Package

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
