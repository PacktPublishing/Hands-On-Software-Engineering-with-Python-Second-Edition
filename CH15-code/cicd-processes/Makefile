# Makefile for Python package project using pyproject.toml and pipenv

# Configurable environment variables
PYPI_REPOSITORY_URL = $(PYPI_REPOSITORY_URL)
TWINE_USERNAME = $(TWINE_USERNAME)
TWINE_PASSWORD = $(TWINE_PASSWORD)

# Ignored pipenv check vulnerabilities (add lines as needed)
IGNORED_PIPENV_CHECKS = \
	--ignore 123 \  # Example: Ignore known vulnerability ID 123 \
	--ignore 456    # Example: Ignore known vulnerability ID 456

.PHONY: cicd-build local-build init test packaging-test build verify check upload clean

# Run the entire pipeline: setup, tests, build, install test, check, upload, clean
cicd-build: init packaging-test test build verify check upload clean

# Run the entire pipeline: setup, tests, build, install test, check, upload, clean
local-build: packaging-test test build verify check clean

init:
	@echo "Initializing environment..."
	# Ensure pipenv environment exists; sync all defined dependency categories from Pipfile.lock
	@pipenv --venv >/dev/null 2>&1 || pipenv sync

packaging-test:
	@echo "Running packaging safety checks..."
	# Run packaging-specific tests (e.g., to check version availability)
	# Assumes PYTHONPATH is defined in a .env file loaded by pipenv
	pipenv run pytest tests/packaging

test:
	@echo "Running unit tests..."
	# Run unit tests in pipenv environment
	pipenv run coverage run -m pytest tests/unit
	# Show a coverage report. There's no set target,
	# but reviewing it after a build is not a bad idea.
	pipenv run coverage report -m

build:
	@echo "Building the package..."
	# Build the package (wheel + sdist) using pyproject.toml
	pipenv run python -m build

verify:
	@echo "Verifying installation in a clean environment..."
	# Create temporary cross-platform-safe directory
	@TMP_ENV=$$(mktemp -d) && \
		# Create virtual environment inside it
		python -m venv $$TMP_ENV/venv && \
		# Activate the new environment
		. $$TMP_ENV/venv/bin/activate && \
		# Install the freshly built wheel
		pip install dist/*.whl && \
		# Run unit tests again inside isolated install
		pytest tests/unit && \
		# Deactivate the temporary venva
		deactivate && \
		# Clean up temporary environment
		rm -rf $$TMP_ENV

check:
	@echo "Running pipenv checks..."
	# Run pipenv safety checks with optional ignores
	pipenv check $(IGNORED_PIPENV_CHECKS)

upload:
	@echo "Uploading package to repository..."
	# Upload built package to configured private repository
	twine upload --repository-url $(PYPI_REPOSITORY_URL) \
	# Authenticate with Twine credentials from environment
		-u $(TWINE_USERNAME) -p $(TWINE_PASSWORD) dist/*

clean:
	@echo "Cleaning up build artifacts..."
	# Remove build output and metadata
	rm -rf build dist *.egg-info
