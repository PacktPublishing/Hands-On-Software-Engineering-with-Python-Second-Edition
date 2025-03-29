# Code to run if the module is executed directly
if __name__ == '__main__':

    import inspect
    import unittest

    from hms.core.data_objects import BaseDataObject

    @unittest.skip('Test stubbed but not yet implemented')
    def test_FIELDNAME_get_happy_paths(self):
        """
        Tests the get process of the FIELDNAME field of the CLASSNAME class
        """
        self.fail('TESTNAME has not been implemented yet')

    @unittest.skip('Test stubbed but not yet implemented')
    def test_FIELDNAME_set_happy_paths(self):
        """
        Tests the set process of the FIELDNAME field of the CLASSNAME class
        """
        self.fail('TESTNAME has not been implemented yet')

    @unittest.skip('Test stubbed but not yet implemented')
    def test_FIELDNAME_set_bad_value(self):
        """
        Tests the validation of the set process of the FIELDNAME field of the CLASSNAME class
        """
        self.fail('TESTNAME has not been implemented yet')

    @unittest.skip('Test stubbed but not yet implemented')
    def test_FIELDNAME_delete_happy_paths(self):
        """
        Tests the delete process of the FIELDNAME field of the CLASSNAME class
        """
        self.fail('TESTNAME has not been implemented yet')

    test_sources = {
        'test_FIELDNAME_get_happy_paths': inspect.getsource(test_FIELDNAME_get_happy_paths),
        'test_FIELDNAME_set_happy_paths': inspect.getsource(test_FIELDNAME_set_happy_paths),
        'test_FIELDNAME_set_bad_value': inspect.getsource(test_FIELDNAME_set_bad_value),
        'test_FIELDNAME_delete_happy_paths': inspect.getsource(test_FIELDNAME_delete_happy_paths),
    }

    test_cases = []

    for cls in (BaseDataObject,):
        CLASSNAME = cls.__name__
        test_cases.append(
            f'''class test_{CLASSNAME}(unittest.TestCase):
    """
    Tests the {CLASSNAME} class.
    """
''')
        for field_name in cls.CRITERIA_FIELDS:
            for name, source in test_sources.items():
                test_cases.append(
                    source.replace('CLASSNAME', cls.__name__)
                    .replace('FIELDNAME', field_name)
                )

    print('\n'.join(test_cases))
