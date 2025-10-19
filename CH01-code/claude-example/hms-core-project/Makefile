.PHONY: clean lint test test-unit test-integration test-system coverage build publish

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
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name "*.eggs" -exec rm -rf {} +
	find . -type d -name "*.pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	@echo "Clean complete!"

# Install dependencies
install:
	$(PIPENV) install --dev

# Lint code
lint:
	@echo "Linting code..."
	$(PIPENV) run flake8 $(SRC_DIR)
	@echo "Lint complete!"

# Run unit tests
test-unit:
	@echo "Running unit tests..."
	$(PIPENV) run pytest $(TEST_DIR)/unit -v
	@echo "Unit tests complete!"

# Run integration tests
test-integration:
	@echo "Running integration tests..."
	$(PIPENV) run pytest $(TEST_DIR)/integration -v
	@echo "Integration tests complete!"

# Run system tests
test-system:
	@echo "Running system tests..."
	$(PIPENV) run pytest $(TEST_DIR)/system -v
	@echo "System tests complete!"

# Run all tests
test: test-unit test-integration test-system
	@echo "All tests complete!"

# Generate coverage report
coverage:
	@echo "Generating coverage report..."
	$(PIPENV) run coverage run -m pytest $(TEST_DIR)
	$(PIPENV) run coverage report -m
	$(PIPENV) run coverage html
	@echo "Coverage report complete!"

# Build package
build: clean lint test
	@echo "Building package..."
	$(PIPENV) run python -m build
	@echo "Build complete!"

# Publish package
publish: build
	@echo "Publishing package..."
	$(PIPENV) run twine check dist/*
	$(PIPENV) run twine upload dist/*
	@echo "Publish complete!"

# Default target
all: clean lint test build
