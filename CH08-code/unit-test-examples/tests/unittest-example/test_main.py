#!/usr/bin/env python3.11
"""
A unit-test suite for the example main.py module, using Python's
built-in unittest module.

Example:
--------
python -m unittest -v tests/unittest-example/test_main.py
"""

import unittest

from main import main_function, MainClass


class test_module_functions(unittest.TestCase):

    def test_main_function(self):
        assert main_function() is None


class test_MainClass(unittest.TestCase):

    def test__init__(self):
        instance = MainClass()

    def test_method(self):
        instance = MainClass()
        self.assertEqual(instance.method(), None)

if __name__ == '__main__':

    unittest.main(verbosity=2)
