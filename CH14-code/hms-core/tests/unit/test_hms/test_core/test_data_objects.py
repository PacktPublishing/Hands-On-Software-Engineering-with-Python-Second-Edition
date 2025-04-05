#!/usr/bin/env python3.11
"""
"""

# Built-In Imports
import json
import os
import unittest

from typing import ClassVar
from unittest.mock import patch, MagicMock

# Third-Party Imports
from mysql.connector.connection_cext import \
    CMySQLConnection

from goblinfish.testing.pact.modules import \
    ExaminesModuleMembers
from goblinfish.testing.pact.module_members import \
    ExaminesSourceClass, ExaminesSourceFunction

from pydantic import BaseModel

from typeguard import TypeCheckError

# Path Manipulations (avoid these!) and "Local" Imports

# Import the test target
from hms.core.data_objects import \
    BaseDataObject, build_limit_clause, \
    build_order_by_clause, build_where_clause, \
    get_env_database_connector, get_examples, \
    SQL_OPERATORS


# Set up a class to test with
class ExampleModel(BaseDataObject, BaseModel):
    pass


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

    def test_get_bad_criteria(self):
        self.fail(
            'test_get_bad_criteria has not been '
            'implemented yet'
        )

    def test_get_bad_db_source_name(self):
        self.fail(
            'test_get_bad_db_source_name has not been '
            'implemented yet'
        )

    def test_get_bad_oids(self):
        self.fail(
            'test_get_bad_oids has not been '
            'implemented yet'
        )

    def test_get_bad_page_number(self):
        self.fail(
            'test_get_bad_page_number has not been '
            'implemented yet'
        )

    def test_get_bad_page_size(self):
        self.fail(
            'test_get_bad_page_size has not been '
            'implemented yet'
        )

    def test_get_happy_paths(self):
        self.fail(
            'test_get_happy_paths has not been '
            'implemented yet'
        )

    def test_from_record_bad_data(self):
        self.fail(
            'test_from_record_bad_data has not been '
            'implemented yet'
        )

    def test_from_record_happy_paths(self):
        self.fail(
            'test_from_record_happy_paths has not been '
            'implemented yet'
        )

    def test_save_bad_db_source_name(self):
        self.fail(
            'test_save_bad_db_source_name has not been '
            'implemented yet'
        )

    @patch.dict(
        os.environ,
        {
            'MYSQL_HOST': 'some-database-host',
            'MYSQL_PORT': '1234',
            'MYSQL_DB': 'some-database-name',
            'MYSQL_USER': 'some-user-name',
            'MYSQL_PASS': 'super-secret-password-really',
        }
    )
    @patch('mysql.connector.connect')
    def test_save_happy_paths(self, mock_connect):
        # Arrange

        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            WRITE_TEMPLATE: ClassVar = '/* This is some SQL */'
            pass

        # Gather up all the possible examples for
        # that class
        examples = get_examples(ConcreteDataObject)

        # Configure the database-related mocks and patches
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.execute.return_value = None        

        for example in examples:
            with self.subTest(
                msg=f'Testing {example} object save'
            ):
                # Arrange (resetting mocks)
                mock_cursor.reset_mock()
                mock_connection.reset_mock()
                mock_connection.cursor.return_value. \
                    __enter__.reset_mock()
                # Act
                inst = ConcreteDataObject(**example)
                inst.save()
                # Assert
                mock_connect.assert_called_once()
                mock_connection.cursor \
                    .assert_called_once()
                mock_cursor.execute \
                        .assert_called_once_with(
                    ConcreteDataObject.WRITE_TEMPLATE,
                    (
                        # The values for the INSERT SQL
                        str(inst.oid),
                        inst.is_active,
                        inst.is_deleted,
                        example['created'],
                        example['modified'],
                        inst.model_dump_json(),
                        # The values for the UPDATE SQL
                        str(inst.oid),
                        inst.is_active,
                        inst.is_deleted,
                        example['created'],
                        example['modified'],
                        inst.model_dump_json(),
                    )
                )
                mock_connection.commit.assert_called_once()

        self.fail(
            'test_save_happy_paths is not complete'
        )


class test_build_limit_clause(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'build_limit_clause'

    valid_arguments = {
        'page_size': (1, 2),
        'page_number': (0, 1),
    }

    invalid_arguments = {
        'page_size': (0, 1.2, 'three'),
        'page_number': (-1, 2.3, 'four'),
    }

    def test_build_limit_clause_bad_page_number(self):
        page_size = self.valid_arguments['page_size'][0]
        for page_number \
                in self.invalid_arguments['page_number']:
            with self.subTest(
                msg=f'Testing page_size {page_size}, '
                f'page_number {page_number}'
            ):
                with self.assertRaises(
                    (AssertionError, TypeCheckError)
                ):
                    build_limit_clause(
                        page_size, page_number
                    )

    def test_build_limit_clause_bad_page_size(self):
        page_number = self.valid_arguments['page_number'][0]  # noqa: E501
        for page_size in \
                self.invalid_arguments['page_size']:
            with self.subTest(
                msg=f'Testing page_size {page_size}, '
                f'page_number {page_number}'
            ):
                with self.assertRaises(
                    (AssertionError, TypeCheckError)
                ):
                    build_limit_clause(
                        page_size, page_number
                    )

    def test_build_limit_clause_happy_paths(self):
        # Arrange
        for page_number in \
                self.valid_arguments['page_number']:
            for page_size \
                    in self.valid_arguments['page_size']:
                with self.subTest(
                    msg=f'Testing page_size {page_size}, '
                    f'page_number {page_number}'
                ):
                    offset = page_size * page_number
                    expected = (
                        f'LIMIT {page_size} '
                        f'OFFSET {offset}'
                    )
                    # Act
                    actual = build_limit_clause(
                        page_size, page_number
                    )
                    # Assert
                    self.assertEqual(
                        actual, expected,
                        f'build_limit_clause({page_size}, '  # noqa: E501
                        f'{page_number}) is expected to '
                        f'return {expected}, but returned '  # noqa: E501
                        f'{actual} instead.'
                    )


class test_build_order_by_clause(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'build_order_by_clause'

    @unittest.skip('Not usefully testable')
    def test_build_order_by_clause_bad_criteria(self):
        # The function will return a usable result even
        # if invalid (disallowed) criteria are passed,
        # and will not raise errors, so it's not really
        # testable in any mainingful way
        self.fail(
            'test_build_order_by_clause_bad_criteria has '
            'not been implemented yet'
        )

    @unittest.skip('Not usefully testable')
    def test_build_order_by_clause_bad_criteria_fields(self):  # noqa: E501
        # The function will return a usable result even
        # if invalid (disallowed) criteria are passed,
        # and will not raise errors, so it's not really
        # testable in any mainingful way
        self.fail(
            'test_build_order_by_clause_bad_criteria_'
            'fields has not been implemented yet'
        )

    def test_build_order_by_clause_happy_paths(self):
        # Act
        expected = 'ORDER BY date desc, count'
        actual = build_order_by_clause(
            {'sort_date': 'desc', 'sort_count': 'asc'},
            ['date', 'count']
        )
        # Assert
        self.assertEqual(actual, expected)

        # Act
        expected = 'ORDER BY count desc, date'
        actual = build_order_by_clause(
            {'sort_count': 'desc', 'sort_date': 'asc'},
            ['date', 'count']
        )
        # Assert
        self.assertEqual(actual, expected)

        # Testing when criteria are not in criteria-list
        # Act
        expected = 'ORDER BY count'
        actual = build_order_by_clause(
            {'sort_count': 'asc', 'sort_date': 'asc'},
            ['count']
        )
        # Assert
        self.assertEqual(actual, expected)


class test_build_where_clause(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'build_where_clause'

    @unittest.skip('Not usefully testable')
    def test_build_where_clause_bad_criteria(self):
        # The function will return a usable result even
        # if invalid (disallowed) criteria are passed,
        # and will not raise errors, so it's not really
        # testable in any mainingful way
        self.fail(
            'test_build_where_clause_bad_criteria has '
            'not been implemented yet'
        )

    @unittest.skip('Not usefully testable')
    def test_build_where_clause_bad_criteria_fields(self):
        # The function will return a usable result even
        # if invalid (disallowed) criteria are passed,
        # and will not raise errors, so it's not really
        # testable in any mainingful way
        self.fail(
            'test_build_where_clause_bad_criteria_fields '
            'has not been implemented yet'
        )

    def test_build_where_clause_happy_paths(self):
        for suffix, operator in SQL_OPERATORS.items():
            # Arrange
            if suffix == '_in':
                criteria = {f'count{suffix}': (1, 2)}
                expected = (
                    'WHERE count IN (%s, %s)', (1, 2)
                )
            else:
                criteria = {f'count{suffix}': 2}
                expected = (
                    f'WHERE count{operator}', (2,)
                )
            with self.subTest(
                msg=f'Testing {suffix} criteria'
            ):
                # Act
                actual = build_where_clause(
                    criteria, ['count']
                )
                # Assert
                self.assertEqual(
                    actual, expected,
                    'Calling build_where_clause with '
                    f'{criteria} was expected to return '
                    f'{expected}, but {actual} was '
                    'returned instead.'
                )


class test_get_env_database_connector(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'get_env_database_connector'

    @patch.dict(
        os.environ,
        {
            'MYSQL_HOST': 'some-database-host',
            'MYSQL_PORT': '1234',
            'MYSQL_DB': 'some-database-name',
            'MYSQL_USER': 'some-user-name',
            'MYSQL_PASS': 'super-secret-password-really',
        }
    )
    @patch('mysql.connector.connect', autospec=True)
    def test_get_env_database_connector_happy_paths(
        self, patch_connection
    ):
        """Test getting a cached database connection."""
        # INITIAL connection retrieval: Arrange
        patch_connection.return_value = CMySQLConnection()
        # Act - initial connection retrieval
        connector = get_env_database_connector()
        # Assert
        patch_connection.assert_called_with(
            host=os.environ['MYSQL_HOST'],
            port=os.environ['MYSQL_PORT'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASS'],
            database=os.environ['MYSQL_DB'],
        )
        # CACHED connection retrieval: Arrange
        patch_connection.reset_mock()
        # Act
        cached_connector = get_env_database_connector()
        # Assert
        patch_connection.assert_not_called()
        self.assertTrue(
            connector is cached_connector,
            'Second and subsequent calls to get_env_'
            'database_connector should return the same '
            f'object, but {connector} and '
            f'{cached_connector} are not the same object.'
        )


class test_get_examples(
    unittest.TestCase,
    ExaminesSourceFunction
):
    TARGET_MODULE = 'hms.core.data_objects'
    TARGET_FUNCTION = 'get_examples'

    def test_get_examples_bad_cls(self):
        # Test that a class that isn't a BaseModel raises
        # an error. There's nothing more to test on this
        # count.
        with self.assertRaises(TypeError):
            get_examples(unittest.TestCase)

    def test_get_examples_bad_max_items(self):
        for bad_item in (2.3, {}, [], object()):
            with self.subTest(
                msg=f'Testing with {bad_item}'
            ):
                with self.assertRaises(
                    (TypeCheckError, TypeError)
                ):
                    get_examples(
                        ExampleModel, max_items=bad_item
                    )

    def test_get_examples_bad_randomize(self):
        for bad_random in (2.3, {}, [], object()):
            with self.subTest(
                msg=f'Testing with {bad_random}'
            ):
                with self.assertRaises(
                    (TypeCheckError, TypeError)
                ):
                    get_examples(
                        ExampleModel, randomize=bad_random
                    )

    def test_get_examples_happy_paths(self):
        # Test that max_items returns only that many items
        all_items = get_examples(ExampleModel)
        max_item_count = len(all_items)
        for i in range(1, max_item_count - 1):
            items = get_examples(
                ExampleModel, max_items=i
            )
            self.assertEqual(len(items), i)
        # Test that randomize randomizes the results
        # It is possible that the two lists will be equal
        # if the examples for the fields in the target
        # model class are too short. To safeguard against
        # that probability, try once per item in the list.
        # If *ANY* of those succeed in being not equal,
        # it's considered good.
        for item in all_items * 2:
            random_items = get_examples(
                ExampleModel, randomize=True
            )
            if [i for i in all_items] \
                    != [i for i in random_items]:
                break
            self.fail(
                f'{len(all_items) * 2} randomized tries '
                'did not arrive at even one difference. '
                'If this happens more than once, some'
                'thing is almost certainly wrong.'
            )


# Code to run if the module is executed directly
if __name__ == '__main__':

    # ~ unittest.main()

    import pytest
    # ~ pytest.main([__file__, '-v'])
    pytest.main([f'{__file__}::test_BaseDataObject', '-v'])  # noqa: E501
