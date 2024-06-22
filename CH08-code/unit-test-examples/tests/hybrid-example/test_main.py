import unittest

import pytest

from main import main_function, MainClass

def test_main_function():
    assert main_function() is None


class test_MainClass(unittest.TestCase):

    def test__init__(self):
        instance = MainClass()

    def test_method(self):
        instance = MainClass()
        self.assertEqual(instance.method(), None)

if __name__ == '__main__':

    pytest.main([__file__, '-vv'])
