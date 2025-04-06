#!/usr/bin/env python3.11
"""
Testing that all source modules have corresponding test
modules in the test suite.
"""

# Built-In Imports
import unittest

# Third-Party Imports
from goblinfish.testing.pact.projects import \
    ExaminesProjectModules

# Path Manipulations (avoid these!) and "Local" Imports


class test_ProjectTestModulesExist(
    unittest.TestCase,
    ExaminesProjectModules
):
    """
    Tests that all source modules have corresponding
    test modules in the test suite.
    """
    pass


# Code to run if the module is executed directly
if __name__ == '__main__':

    unittest.main()
