#!/usr/bin/env python3.11
"""
"""

# Built-In Imports
import unittest

# Third-Party Imports
from goblinfish.testing.pact.modules import \
    ExaminesModuleMembers
from goblinfish.testing.pact.module_members import \
    ExaminesSourceClass, ExaminesSourceFunction

# Path Manipulations (avoid these!) and "Local" Imports

# Import the test target
from hms.core.data_objects import \
    BaseDataObject, build_limit_clause, \
    build_order_by_clause, build_where_clause, \
    get_env_database_connector


# Source-to-test-module correspondance test
class test_ProjectTestMembersExist(
    unittest.TestCase,
    ExaminesModuleMembers
):
    """
    Tests that all source module members have
    corresponding test module members in this
    test module.
    """
    TARGET_MODULE = 'hms.core.data_objects'


# Expected test-case classes
class test_BaseDataObject(
    unittest.TestCase,
    ExaminesSourceClass
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_CLASS = 'BaseDataObject'

    # Test-methods for source properties and fields
    @unittest.skip('Test stubbed but not yet implemented')
    def test_oid_get_happy_paths(self):
        """
        Tests the get process of the oid field of the
        BaseDataObject class
        """
        self.fail(
            'test_oid_get_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_oid_set_happy_paths(self):
        """
        Tests the set process of the oid field of the
        BaseDataObject class
        """
        self.fail(
            'test_oid_set_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_oid_set_bad_value(self):
        """
        Tests the validation of the set process of the
        oid field of the BaseDataObject class
        """
        self.fail(
            'test_oid_set_bad_value has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_oid_delete_happy_paths(self):
        """
        Tests the delete process of the oid field of the
        BaseDataObject class
        """
        self.fail(
            'test_oid_delete_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_is_active_get_happy_paths(self):
        """
        Tests the get process of the is_active field of
        the BaseDataObject class
        """
        self.fail(
            'test_is_active_get_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_is_active_set_happy_paths(self):
        """
        Tests the set process of the is_active field of
        the BaseDataObject class
        """
        self.fail(
            'test_is_active_set_happy_paths has not '
            'been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_is_active_set_bad_value(self):
        """
        Tests the validation of the set process of the
        is_active field of the BaseDataObject class
        """
        self.fail(
            'test_is_active_set_bad_value has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_is_active_delete_happy_paths(self):
        """
        Tests the delete process of the is_active field
        of the BaseDataObject class
        """
        self.fail(
            'test_is_active_delete_happy_paths has not '
            'been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_is_deleted_get_happy_paths(self):
        """
        Tests the get process of the is_deleted field of
        the BaseDataObject class
        """
        self.fail(
            'test_is_deleted_get_happy_paths has not '
            'been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_is_deleted_set_happy_paths(self):
        """
        Tests the set process of the is_deleted field of
        the BaseDataObject class
        """
        self.fail(
            'test_is_deleted_set_happy_paths has not '
            'been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_is_deleted_set_bad_value(self):
        """
        Tests the validation of the set process of the
        is_deleted field of the BaseDataObject class
        """
        self.fail(
            'test_is_deleted_set_bad_value has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_is_deleted_delete_happy_paths(self):
        """
        Tests the delete process of the is_deleted field
        of the BaseDataObject class
        """
        self.fail(
            'test_is_deleted_delete_happy_paths has not '
            'been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_created_get_happy_paths(self):
        """
        Tests the get process of the created field of the
        BaseDataObject class
        """
        self.fail(
            'test_created_get_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_created_set_happy_paths(self):
        """
        Tests the set process of the created field of the
        BaseDataObject class
        """
        self.fail(
            'test_created_set_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_created_set_bad_value(self):
        """
        Tests the validation of the set process of the
        created field of the BaseDataObject class
        """
        self.fail(
            'test_created_set_bad_value has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_created_delete_happy_paths(self):
        """
        Tests the delete process of the created field of
        the BaseDataObject class
        """
        self.fail(
            'test_created_delete_happy_paths has not '
            'been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_modified_get_happy_paths(self):
        """
        Tests the get process of the modified field of
        the BaseDataObject class
        """
        self.fail(
            'test_modified_get_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_modified_set_happy_paths(self):
        """
        Tests the set process of the modified field of
        the BaseDataObject class
        """
        self.fail(
            'test_modified_set_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_modified_set_bad_value(self):
        """
        Tests the validation of the set process of the
        modified field of the BaseDataObject class
        """
        self.fail(
            'test_modified_set_bad_value has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_modified_delete_happy_paths(self):
        """
        Tests the delete process of the modified field of
        the BaseDataObject class
        """
        self.fail(
            'test_modified_delete_happy_paths has not '
            'been implemented yet'
        )

    # Test-methods for source methods
    @unittest.skip('Test stubbed but not yet implemented')
    def test_delete_happy_paths(self):
        self.fail(
            'test_delete_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_get_happy_paths(self):
        self.fail(
            'test_get_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_from_record_bad_data(self):
        self.fail(
            'test_from_record_bad_data has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_from_record_happy_paths(self):
        self.fail(
            'test_from_record_happy_paths has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_get_bad_criteria(self):
        self.fail(
            'test_get_bad_criteria has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_get_bad_db_source_name(self):
        self.fail(
            'test_get_bad_db_source_name has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_get_bad_oids(self):
        self.fail(
            'test_get_bad_oids has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_get_bad_page_number(self):
        self.fail(
            'test_get_bad_page_number has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_get_bad_page_size(self):
        self.fail(
            'test_get_bad_page_size has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_save_bad_db_source_name(self):
        self.fail(
            'test_save_bad_db_source_name has not been '
            'implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_save_happy_paths(self):
        self.fail(
            'test_save_happy_paths has not been '
            'implemented yet'
        )


class test_build_limit_clause(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'build_limit_clause'

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_limit_clause_bad_page_number(self):
        self.fail(
            'test_build_limit_clause_bad_page_number has '
            'not been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_limit_clause_bad_page_size(self):
        self.fail(
            'test_build_limit_clause_bad_page_size has '
            'not been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_limit_clause_happy_paths(self):
        self.fail(
            'test_build_limit_clause_happy_paths has not '
            'been implemented yet'
        )


class test_build_order_by_clause(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'build_order_by_clause'

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_order_by_clause_bad_criteria(self):
        self.fail(
            'test_build_order_by_clause_bad_criteria has '
            'not been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_order_by_clause_bad_criteria_fields(self):  # noqa: E501
        self.fail(
            'test_build_order_by_clause_bad_criteria_'
            'fields has not been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_order_by_clause_happy_paths(self):
        self.fail(
            'test_build_order_by_clause_happy_paths has '
            'not been implemented yet'
        )


class test_build_where_clause(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'build_where_clause'

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_where_clause_bad_criteria(self):
        self.fail(
            'test_build_where_clause_bad_criteria has '
            'not been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_where_clause_bad_criteria_fields(self):
        self.fail(
            'test_build_where_clause_bad_criteria_fields '
            'has not been implemented yet'
        )

    @unittest.skip('Test stubbed but not yet implemented')
    def test_build_where_clause_happy_paths(self):
        self.fail(
            'test_build_where_clause_happy_paths has not '
            'been implemented yet'
        )


class test_get_env_database_connector(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'get_env_database_connector'

    @unittest.skip('Test stubbed but not yet implemented')
    def test_get_env_database_connector_happy_paths(self):
        self.fail(
            'test_get_env_database_connector_happy_paths '
            'has not been implemented yet'
        )


# Code to run if the module is executed directly
if __name__ == '__main__':

    unittest.main()
