.PHONY: test unit integration system lint coverage build publish

unit:
	pytest tests/unit

integration:
	pytest tests/integration

system:
	pytest tests/system

test: unit integration system

lint:
	flake8 src tests

coverage:
	coverage run -m pytest
	coverage report -m

build:
	python -m build

publish:
	twine upload dist/*
