"""
A dummy test-module, created so that a test-suite can be executed with

pipenv run pytest tests/unit

This module can also be run itself, assuming that the IDE supports that.
"""

import pytest

from example_project.main import CONSTANT


def test_nothing():
    """A dummy test, so that pytest can run without error"""
    assert CONSTANT


if __name__ == '__main__':
    pytest.main([__file__, '-vv'])
