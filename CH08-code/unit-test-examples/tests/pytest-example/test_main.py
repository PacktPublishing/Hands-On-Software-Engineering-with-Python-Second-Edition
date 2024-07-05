#!/usr/bin/env python3.11
"""
A unit-test suite for the example main.py module, using pytest.

Example:
--------
pytest -v tests/pytest-example/test_main.py
"""

import pytest

from main import main_function, MainClass

def test_main_function():
    assert main_function() is None


def test_MainClass__init__():
    instance = MainClass()


def test_MainClass_method():
    instance = MainClass()
    assert instance.method() is None


if __name__ == '__main__':

    pytest.main([__file__, '-vv'])
