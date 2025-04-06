#!/usr/bin/env python3.11
"""
"""

# Built-In Imports
import json
import os
import unittest

from datetime import datetime
from typing import ClassVar
from unittest.mock import patch, MagicMock
from uuid import UUID

# Third-Party Imports
from mysql.connector.connection_cext import \
    CMySQLConnection

from goblinfish.testing.pact.modules import \
    ExaminesModuleMembers
from goblinfish.testing.pact.module_members import \
    ExaminesSourceClass, ExaminesSourceFunction

from pydantic import BaseModel, Field, ValidationError

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

    class ConcreteDataObject(BaseDataObject, BaseModel):
        pass

    EXAMPLE_ARGS = get_examples(
        ConcreteDataObject,
        max_items=1
    )[0]

    # Test-methods for source properties and fields
    def test_oid(self):
        """
        Tests the oid field of the BaseDataObject class
        """
        # Arrange
        good_values = self.ConcreteDataObject.oid.examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'oid'
        }
        for oid in good_values:
            with self.subTest(
                msg=f'Testing creation with oid {oid} '
                f'({type(oid).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                args['oid'] = oid
                if isinstance(oid, str):
                    expected = UUID(oid)
                else:
                    expected = oid
                # Act
                inst = self.ConcreteDataObject(**args)
                # Assert
                self.assertEqual(
                    inst.oid, expected,
                    'Creating a ConcreteDataObject '
                    f'with an oid value of "{oid}" '
                    f'({type(oid).__name__}) should '
                    'return that value in instance.oid, '
                    f'but "{inst.oid}" '
                    f'({type(oid).__name__}) was '
                    'returned instead.'
                )
        with self.subTest(msg='Testing default value'):
            # Arrange
            args = dict(base_args)
            # Act
            inst = self.ConcreteDataObject(**args)
            # Assert
            self.assertTrue(isinstance(inst.oid, UUID))
        with self.subTest(
            msg='Testing that an oid cannot be changed '
            'after it is set'
        ):
            with self.assertRaises(ValidationError):
                inst.oid = UUID('0'*32)
        with self.subTest(
            msg='Testing that an oid cannot be deleted'
        ):
            with self.assertRaises(ValidationError):
                del inst.oid

    def test_is_active(self):
        """
        Tests the is_active field of the BaseDataObject class
        """
        # Arrange
        good_values = self.ConcreteDataObject.is_active.examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'is_active'
        }
        for is_active in good_values:
            with self.subTest(
                msg='Testing creation with is_active '
                f'{is_active} ({type(is_active).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['is_active'] = is_active
                # Act
                inst = self.ConcreteDataObject(**args)
                # Assert
                self.assertEqual(
                    inst.is_active, expected,
                    'Creating a ConcreteDataObject with '
                    f'an is_active value of '
                    f'"{is_active}" '
                    f'({type(is_active).__name__}) '
                    'should return that value in instance'
                    f'.is_active, but "{inst.is_active}" '
                    f'({type(is_active).__name__}) was '
                    'returned instead.'
                )
        with self.subTest(msg='Testing default value'):
            # Arrange
            args = dict(base_args)
            # Act
            inst = self.ConcreteDataObject(**args)
            # Assert
            self.assertFalse(inst.is_active)
            self.assertTrue(
                isinstance(inst.is_active, bool)
            )

    def test_is_deleted(self):
        """
        Tests the is_deleted field of the BaseDataObject class
        """
        # Arrange
        good_values = self.ConcreteDataObject.is_deleted.examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'is_deleted'
        }
        for is_deleted in good_values:
            with self.subTest(
                msg='Testing creation with is_deleted '
                f'{is_deleted} '
                f'({type(is_deleted).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['is_deleted'] = is_deleted
                # Act
                inst = self.ConcreteDataObject(**args)
                # Assert
                self.assertEqual(
                    inst.is_deleted, expected,
                    'Creating a ConcreteDataObject with '
                    'an is_deleted value of '
                    f'"{is_deleted}" '
                    f'({type(is_deleted).__name__}) '
                    'should return that value in instance'
                    '.is_deleted, but '
                    f'"{inst.is_deleted}" '
                    f'({type(is_deleted).__name__}) was '
                    'returned instead.'
                )
        with self.subTest(msg='Testing default value'):
            # Arrange
            args = dict(base_args)
            # Act
            inst = self.ConcreteDataObject(**args)
            # Assert
            self.assertFalse(inst.is_deleted)
            self.assertTrue(
                isinstance(inst.is_deleted, bool)
            )

    def test_created(self):
        """
        Tests the created field of the BaseDataObject class
        """
        # Arrange
        good_values = self.ConcreteDataObject.created.examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'created'
        }
        for created in good_values:
            with self.subTest(
                msg=f'Testing creation with created '
                f'{created} ({type(created).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['created'] = \
                    datetime.utcnow()
                # Act
                inst = self.ConcreteDataObject(**args)
                # Assert
                self.assertEqual(
                    inst.created, expected,
                    'Creating a ConcreteDataObject with '
                    f'a created value of "{created}" '
                    f'({type(created).__name__}) '
                    'should return that value in instance'
                    f'.created, but "{inst.created}" '
                    f'({type(created).__name__}) was '
                    'returned instead.'
                )
        with self.subTest(msg='Testing default value'):
            # Arrange
            args = dict(base_args)
            # Act
            inst = self.ConcreteDataObject(**args)
            # Assert
            self.assertTrue(inst.created)
            self.assertTrue(
                isinstance(inst.created, datetime)
            )
        with self.subTest(
            msg='Testing that a created cannot be '
            'changed after it is set'
        ):
            with self.assertRaises(ValidationError):
                inst.created = datetime.utcnow()
        with self.subTest(
            msg='Testing that n created cannot be deleted'
        ):
            with self.assertRaises(ValidationError):
                del inst.created

    def test_modified(self):
        """
        Tests the modified field of the BaseDataObject class
        """
        # Arrange
        good_values = self.ConcreteDataObject.modified.examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'modified'
        }
        for modified in good_values:
            with self.subTest(
                msg=f'Testing creation with modified '
                f'{modified} ({type(modified).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['modified'] = \
                    datetime.utcnow()
                # Act
                inst = self.ConcreteDataObject(**args)
                # Assert
                self.assertEqual(
                    inst.modified, expected,
                    'Creating a ConcreteDataObject with '
                    f'a modified value of "{modified}" '
                    f'({type(modified).__name__}) '
                    'should return that value in instance'
                    f'.modified, but "{inst.modified}" '
                    f'({type(modified).__name__}) was '
                    'returned instead.'
                )
        with self.subTest(msg='Testing default value'):
            # Arrange
            args = dict(base_args)
            # Act
            inst = self.ConcreteDataObject(**args)
            # Assert
            self.assertEqual(inst.modified, None)

    # Test-methods for source methods
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
    @patch(
        'hms.core.data_objects.get_env_database_connector'
    )
    def test_delete_happy_paths(self, mock_connect):
        # Arrange
        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            DELETE_TEMPLATE: ClassVar = 'DELETE FROM ' \
                '{TABLE_NAME} {WHERE}'
            TABLE_NAME: ClassVar = 'no_such_table'
            given_name: str = Field()
            family_name: str = Field()

        # Configure the database-related mocks and patches
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Test single oid
        with self.subTest(msg='Test with single oid (str)'):
            ConcreteDataObject.delete(
                '00000000-0000-0000-0000-000000000001'
            )
            mock_cursor.execute.assert_called_once_with(
                'DELETE FROM no_such_table '
                'WHERE oid = %s',
                ('00000000-0000-0000-0000-000000000001',)
            )
        with self.subTest(
            msg='Test with single oid (UUID)'
        ):
            mock_cursor.reset_mock()
            ConcreteDataObject.delete(
                UUID(
                    '00000000-0000-0000-0000-000000000001'
                )
            )
            mock_cursor.execute.assert_called_once_with(
                'DELETE FROM no_such_table '
                'WHERE oid = %s',
                ('00000000-0000-0000-0000-000000000001',)
            )

        # ~ with self.subTest(msg='Test with multiple oids'):

    @unittest.skip(
        'Test in integration; too many variables to '
        'test here.'
    )
    def test_get_bad_criteria(self):
        self.fail(
            'test_get_bad_criteria has not been '
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
    @patch(
        'hms.core.data_objects.get_env_database_connector'
    )
    def test_get_bad_db_source_name(self, mock_connect):
        # Arrange
        bad_source_names = (
            1, 2.3, True,
            dict(), list(), tuple(),
            object()
        )
        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            WRITE_TEMPLATE: ClassVar = \
                '/* This is some SQL */'
        # Act/Assert
        for source_name in bad_source_names:
            with self.subTest(
                msg=f'Testing with "{source_name}" '
                f'({type(source_name).__name__}) for source_name'
            ):
                with self.assertRaises(
                    TypeCheckError,
                    msg=f'"{source_name}" '
                    f'({type(source_name).__name__}) '
                    'should raise a typeguard.'
                    'TypeCheckError'
                ):
                    ConcreteDataObject.get(db_source_name=source_name)

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
    @patch(
        'hms.core.data_objects.get_env_database_connector'
    )
    def test_get_bad_oids(self, mock_connect):

        # Arrange
        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            GET_TEMPLATE: ClassVar = 'SELECT * ' \
                'FROM {TABLE_NAME} ' \
                '{WHERE}{ORDER_BY}{LIMIT}'
            TABLE_NAME: ClassVar = 'no_such_table'
            given_name: str = Field()
            family_name: str = Field()

        # Configure the database-related mocks and patches
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        with self.assertRaises(ValueError):
            ConcreteDataObject.get('oid')

        with self.assertRaises(ValueError):
            ConcreteDataObject.get('oid', 'oid')

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
    @patch(
        'hms.core.data_objects.get_env_database_connector'
    )
    def test_get_bad_page_number(self, mock_connect):

        # Arrange
        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            GET_TEMPLATE: ClassVar = 'SELECT * ' \
                'FROM {TABLE_NAME} ' \
                '{WHERE}{ORDER_BY}{LIMIT}'
            TABLE_NAME: ClassVar = 'no_such_table'
            given_name: str = Field()
            family_name: str = Field()

        # Configure the database-related mocks and patches
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        with self.assertRaises(ValueError):
            ConcreteDataObject.get(
                page_size=10, page_number=-1
            )

        with self.assertRaises(TypeCheckError):
            ConcreteDataObject.get(
                page_size=10, page_number='zero'
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
    @patch(
        'hms.core.data_objects.get_env_database_connector'
    )
    def test_get_bad_page_size(self, mock_connect):
        # Arrange
        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            GET_TEMPLATE: ClassVar = 'SELECT * ' \
                'FROM {TABLE_NAME} ' \
                '{WHERE}{ORDER_BY}{LIMIT}'
            TABLE_NAME: ClassVar = 'no_such_table'
            given_name: str = Field()
            family_name: str = Field()

        # Configure the database-related mocks and patches
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        with self.assertRaises(ValueError):
            ConcreteDataObject.get(
                page_size=-1, page_number=0
            )

        with self.assertRaises(TypeCheckError):
            ConcreteDataObject.get(
                page_size='one', page_number=0
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
    @patch(
        'hms.core.data_objects.get_env_database_connector'
    )
    def test_get_happy_paths(self, mock_connect):
        # Arrange
        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            GET_TEMPLATE: ClassVar = 'SELECT * ' \
                'FROM {TABLE_NAME} ' \
                '{WHERE}{ORDER_BY}{LIMIT}'
            TABLE_NAME: ClassVar = 'no_such_table'
            given_name: str = Field()
            family_name: str = Field()

        # Configure the database-related mocks and patches
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Test with criteria
        with self.subTest(msg='Testing with criteria'):
            ConcreteDataObject.get(
                family_name_eq='Jones'
            )
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM no_such_table WHERE '
                'family_name = %s',
                ('Jones',)
            )
            ConcreteDataObject.get(
                given_name_eq='John',
            )
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM no_such_table WHERE '
                'given_name = %s',
                ('John',)
            )
            ConcreteDataObject.get(
                given_name_eq='John',
                family_name_eq='Jones'
            )
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM no_such_table WHERE '
                'given_name = %s AND family_name = %s',
                ('John', 'Jones')
            )
        # TODO: Test with all the other operators in
        #       data_objects.SQL_OPERATORS

        # Test with db_source_name
        with self.subTest(msg='Testing with criteria'):
            ConcreteDataObject.get(
                db_source_name='some_other_table',
                family_name_eq='Jones'
            )
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM some_other_table WHERE '
                'family_name = %s',
                ('Jones',)
            )

        with self.subTest(msg='Testing with oids'):
            ConcreteDataObject.get(
                '00000000-0000-0000-0000-000000000000',
                UUID('00000000-0000-0000-0000-000000000001'),
            )
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM no_such_table '
                'WHERE oid IN (%s, %s)',
                (
                    '00000000-0000-0000-0000-000000000000',
                    '00000000-0000-0000-0000-000000000001',
                )
            )
            ConcreteDataObject.get(
                '00000000-0000-0000-0000-000000000002'
            )
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM no_such_table '
                'WHERE oid = %s',
                ('00000000-0000-0000-0000-000000000002',)
            )
            ConcreteDataObject.get(
                UUID('00000000-0000-0000-0000-000000000003')
            )
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM no_such_table '
                'WHERE oid = %s',
                ('00000000-0000-0000-0000-000000000003',)
            )

        with self.subTest(msg='Testing with page_number only'):
            with self.assertRaises(TypeError):
                ConcreteDataObject.get(page_number=1)

        with self.subTest(msg='Testing with page_size only'):
            ConcreteDataObject.get(page_size=10)
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM no_such_table '
                'LIMIT 10 OFFSET 0'
            )

        # Test with page_number and page_size
        with self.subTest(msg='Testing with page_number and page_size'):
            ConcreteDataObject.get(page_size=10, page_number=1)
            mock_cursor.execute.assert_called_with(
                'SELECT * FROM no_such_table '
                'LIMIT 10 OFFSET 10'
            )

    def test_from_record_bad_data(self):
        bad_data = (
            1, 2.3, 'four', True,
            dict(), list(), tuple(), object()
        )
        for data in bad_data:
            with self.subTest(
                msg=f'Testing with "{data}" '
                f'({type(data).__name__}).'
            ):
                with self.assertRaises(TypeCheckError):
                    BaseDataObject.from_record(data)

    @unittest.skip(
        'Test in integration; too many variables to '
        'test here.'
    )
    def test_from_record_happy_paths(self):
        self.fail(
            'test_from_record_happy_paths has not been '
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
    def test_save_bad_db_source_name(self, db_connection):
        # Arrange
        bad_source_names = (
            1, 2.3, True,
            dict(), list(), tuple(),
            object()
        )
        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            WRITE_TEMPLATE: ClassVar = \
                '/* This is some SQL */'
        inst = ConcreteDataObject()
        # Act/Assert
        for source_name in bad_source_names:
            with self.subTest(
                msg=f'Testing with "{source_name}" '
                f'({type(source_name).__name__}) for source_name'
            ):
                with self.assertRaises(
                    TypeCheckError,
                    msg=f'"{source_name}" '
                    f'({type(source_name).__name__}) '
                    'should raise a typeguard.'
                    'TypeCheckError'
                ):
                    inst.save(db_source_name=source_name)

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
    @patch(
        'hms.core.data_objects.get_env_database_connector'
    )
    def test_save_happy_paths(self, mock_connect):
        # Arrange

        # - A class that implements BaseDataObject
        #   and BaseModel
        class ConcreteDataObject(
            BaseDataObject, BaseModel
        ):
            WRITE_TEMPLATE: ClassVar = '/* This is some SQL */'

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
                # Reset mocks and cache for other tests
                mock_cursor.reset_mock()
                mock_connection.reset_mock()
                mock_connection.cursor.return_value. \
                    __enter__.reset_mock()
                mock_connect.reset_mock()
                mock_connect.cache_clear()


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
        patch_connection.assert_called_once_with(
            host=os.environ['MYSQL_HOST'],
            port=os.environ['MYSQL_PORT'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASS'],
            database=os.environ['MYSQL_DB'],
        )
        # CACHED connection retrieval: Arrange
        # Act
        cached_connector = get_env_database_connector()
        # Assert
        # Do not try to test the underlying cached
        # call, it's mocked out of existance.
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
    # ~ pytest.main([f'{__file__}::test_BaseDataObject::test_modified', '-vv'])  # noqa: E501
