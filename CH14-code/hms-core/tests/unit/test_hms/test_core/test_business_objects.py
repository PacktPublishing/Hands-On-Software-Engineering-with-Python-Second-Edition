import unittest

def test_failing_test_function():
    assert False, 'Force a failure in test_failing_test_function'

class test_tests_exist(unittest.TestCase):
    def test_yep_i_exist(self):
        self.fail('Force a failure in test_tests_exist')

class Test_pytestClass:
    def test_yep_pytest_runs_this(self):
        assert False, 'Force a failure in test_pytestClass'

    def Test_uppercase_method_name(self):
        assert False, 'Force a failure in Test_uppercase_method_name'
