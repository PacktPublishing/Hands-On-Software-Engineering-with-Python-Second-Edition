#!/usr/bin/env python3.11
"""
Provides classes and functionality for defining and
working with businbess-object classes whose state-data
is persisted in a back-end data-store.
"""
from __future__ import annotations

# Built-In Imports
import abc
import json
import os

from datetime import datetime
from functools import cache
from typing import Any, ClassVar, Self
from uuid import UUID, uuid4

# Third-Party Imports
import mysql.connector

from pydantic import BaseModel, Field

from mysql.connector.connection_cext import CMySQLConnection

# Path Manipulations (avoid these!) and "Local" Imports

# Module "Constants" and Other Attributes
SQL_OPERATORS = {
    '_eq': ' = %s',
    '_neq': ' != %s',
    '_gt': ' > %s',
    '_gte': ' >= %s',
    '_lt': ' < %s',
    '_lte': ' <= %s',
    '_like':  'LIKE %s',
    '_in': ' IN %s',
}

# Module Custom Exceptions


# Module Functions
def build_where_clause(
    criteria: dict[str, None],
    criteria_fields: list[str],
) -> tuple[str, tuple[Any]]:
    """
    Builds and returns a SQL `WHERE` clause based on
    the provided criteria.

    Parameters:
    -----------
    criteria : dict
        The criteria provided to a BaseDataObject.get
        call that selection criteria will be extracted
        from.
    criteria_fields : list[str]
        The names of the criteria fields allowed in a
        query, typically provided by the calling object's
        CRITERIA_FIELDS class attribute.
    """
    # If there are no criteria supplied, we can just
    # return something empty, exiting early.
    if not criteria:
        return ('', tuple())

    # Otherwise, we need to generate the WHERE clause
    # and the related parameters
    # - Get the relevant criteria key/value pairs
    actual_criteria = {
        key: value for key, value in criteria.items()
        if key in criteria_fields
        or any(
            [
                key.endswith(op_name)
                for op_name in SQL_OPERATORS
                if op_name
            ]
        )
    }
    # - Build the clause and parameters, starting with
    # an empty list of the values that they'll eventually
    # contain
    where = []
    parameters = []

    # Iterate over the actual criteria items...
    for field, value in actual_criteria.items():
        if field in criteria_fields:
            # If it's not suffixed, just add it
            where.append(f'{field} = %s')
            parameters.append(value)
        else:
            # Otherwise, handle it based on the operator
            # that is specified for the field
            for op_key, op_value in SQL_OPERATORS.items():
                if field.endswith(op_key):
                    # Use the non-suffixed field-name
                    field_name = field[0:-len(op_key)]
                    # "IN" values have to be broken out as
                    # individual values for parameterized
                    # query usage.
                    if op_key == '_in':
                        # Make sure the value is a list
                        # or tuple
                        assert isinstance(
                            value, (list, tuple)
                        ), (
                            '"_in" criteria must be '
                            'supplied as a list or tuple, '
                            f'but {value} is a '
                            f'{type(value).__name__}.'
                        )
                        # Generate the placeholders for
                        # the WHERE clause
                        placeholder_list = ', '.join(
                            ['%s'] * len(value)
                        )
                        where.append(
                            f'{field_name} IN '
                            f'({placeholder_list})'
                        )
                        # Append the value-items to the
                        # parameters
                        parameters += list(value)
                    else:
                        # All the other operations can use
                        # the simple placeholder values in
                        # the global SQL_OPERATORS
                        where.append(
                            f'{field_name}{op_value}'
                        )
                        parameters.append(value)
                    break
                # TODO: Consider raising an error here
                # for unsupported operations?

    # - Finalize the values and return them
    where = 'WHERE ' + ' AND '.join(where)
    parameters = tuple(parameters)
    return (where, parameters)


def build_limit_clause(page_size: int, page_number: int) -> str:
    """
    Creates and returns a LIMIT {page_size} OFFSET {offset}
    clause, intended to be used by the BaseDataObject.get
    class method to facilitate pagination of records.

    Parameters:
    -----------
    page_size : int
        The number of records to be retrieved per "page"
    page_number : int
        The "page" number of page_size records
    """
    assert page_size > 0, \
        'build_limit_clause expects a positive ' \
        f'page_size value, but {page_size} was passed.'
    assert page_number >= 0, \
        'build_limit_clause expects a non-negative ' \
        f'page_size value, but {page_number} was passed.'
    offset = page_size * page_number
    return f'LIMIT {page_size} OFFSET {offset}'


def build_order_by_clause(
    criteria: dict[str, None],
    criteria_fields: list[str],
) -> str:
    """
    Builds and returns a SQL `ORDER BY` clause based on
    the provided criteria.

    Parameters:
    -----------
    criteria : dict
        The criteria provided to a BaseDataObject.get
        call that sort-order criteria will be extracted
        from.
    criteria_fields : list[str]
        The names of the sort fields allowed in a query,
        typically provided by the calling object's
        CRITERIA_FIELDS class attribute.
    """
    # Exit immediately if there are no criteria values
    # specified
    if not criteria:
        return ''
    # Extract the sort fields and their values
    sort_fields = {
        key[5:]: value for key, value in criteria.items()
        if key.startswith('sort_')
        and key[5:] in criteria_fields
    }
    sort_phrases = [
        f'{key} {value if value.lower() == "desc" else ""}'.strip()
        for key, value in sort_fields.items()
    ]
    if sort_phrases:
        return f'ORDER BY {", ".join(sort_phrases)}'
    return ''


@cache
def get_env_database_connector() -> CMySQLConnection:
    """
    Creates, caches and returns a MySQL connector object,
    supporting cursors, suitable for making requests
    against the database specified in the environment.

    Environment:
    ------------
    MYSQL_HOST : str
        The host name of the MySQL server to
        connect to.
    MYSQL_PORT : int
        The network port of the MySQL server to
        connect to.
    MYSQL_USER : str
        The account name to use to connect to
        the MySQL server.
    MYSQL_PASS : str
        The password to use to connect to the
        MySQL server.
    MYSQL_DB : str
        The name of the database to connect to
        on the MySQL server.

    Notes:
    ------
    Environment variables can be set locally for
    development purposes, but will be managed in a
    more secure fashion in production.
    """
    connector = mysql.connector.connect(
        host=os.environ['MYSQL_HOST'],
        port=os.environ['MYSQL_PORT'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASS'],
        database=os.environ['MYSQL_DB'],
    )
    return connector

# Module Metaclasses


# Module Abstract Base Classes
class BaseDataObject(metaclass=abc.ABCMeta):
    """
    Provides baseline functionality, interface requirements and type identity for objects that can persist their state data in a back-end RDBMS data store.
    """  # noqa: E501

    TABLE_NAME: ClassVar[str] = None
    CRITERIA_FIELDS: ClassVar[list[str]] = [
        'oid', 'is_active', 'is_deleted',
        'created', 'modified'
    ]
    DELETE_TEMPLATE: ClassVar[str] = (
        'DELETE FROM {TABLE_NAME} {WHERE};'
    )
    GET_TEMPLATE: ClassVar[str] = (
        'SELECT * FROM {TABLE_NAME} '
        '{WHERE} {ORDER_BY} {LIMIT};'
    )
    WRITE_TEMPLATE: ClassVar[str] = (
        'INSERT INTO {TABLE_NAME} '
        '({FIELD_NAMES}) VALUES ({FIELD_VALUES}) '
        'ON DUPLICATE KEY UPDATE '
        '{UPDATE_NAMES_VALUES};'
    )

    oid: UUID = Field(
        title='Object ID',
        description='The unique identifier of the record '
        'for the instance\'s state data in the back end '
        'data store',
        examples=[
            UUID('0'*32),
            '073f2f01-64b6-441f-a053-b3aaa3cf5a1e',
            UUID('f'*32),
        ],
        default_factory=uuid4, frozen=True,
    )
    is_active: bool = Field(
        title='Is Active',
        description='Flag indicating whether the object '
        'is "active."',
        examples=[False, True],
        default=False
    )
    is_deleted: bool = Field(
        title='Is Deleted',
        description='Flag indicating whether the object '
        'is "deleted" (pending an **actual** deletion '
        'later, perhaps).',
        examples=[False, True],
        default=False,
    )
    created: datetime = Field(
        title='Created Date',
        description='The date/time (UTC) when the object '
        'was created.',
        examples=['2025-01-04T14:52:39.842206'],
        default_factory=datetime.utcnow, frozen=True,
    )
    modified: datetime | None = Field(
        title='Last Modified Date',
        description='The (optional) date/time (UTC) when '
        'the object was last modified.',
        examples=[None, '2025-01-04T14:52:39.842206'],
        default=None,
    )

    def save(self, *, db_source_name: str | None = None) -> None:
        """
        Saves the instance's state data to the back end
        data store.

        Parameters:
        -----------
        db_source_name : Optional str
            The name of an alternative table to execute
            the query against during the save.
        """
        field_data = {
            key: value for key, value
            in self.model_dump(mode='json').items()
            if key in self.CRITERIA_FIELDS
        }
        field_data['object_state'] = self.model_dump_json()
        field_names = []
        field_placeholders = []
        field_values = []
        update_names = []
        update_values = []
        for key, value in field_data.items():
            field_names.append(key)
            field_values.append(value)
            field_placeholders.append('%s')
            update_names.append(f'{key} = %s')
            update_values.append(value)
        final_sql = self.WRITE_TEMPLATE.format(
            TABLE_NAME=db_source_name
            or self.__class__.TABLE_NAME,
            FIELD_NAMES=', '.join(field_names),
            FIELD_VALUES=', '.join(field_placeholders),
            UPDATE_NAMES_VALUES=', '.join(update_names),
        )
        parameters = tuple(field_values + update_values)

        # Get the connector, create a cursor, execute the
        # query (with parameters if any are supplied)
        connector = get_env_database_connector()
        with connector.cursor() as cursor:
            if parameters:
                cursor.execute(final_sql, parameters)
            else:
                cursor.execute(final_sql)
        connector.commit()

    @classmethod
    def from_record(
        cls,
        data: dict[str, Any] | tuple[tuple[str, Any]]
    ) -> BaseModel:
        """
        Creates and returns an instance of the class from
        either of the common record-structure return-types
        from a back-end data-store.

        Parameters:
        -----------
        data : dict, or tuple of tuples
            The state representation of the object to
            create from query results against a data
            store. Expected to be either a dict of field
            names and values, or a tuple of key/value
            tuples that can be converted to such a dict
        """
        if isinstance(data, tuple):
            data = dict(data)
        return cls(**data)

    @classmethod
    def get(
        cls,
        *oids: list[UUID | str],
        db_source_name: str | None = None,
        page_size: int | None = None,
        page_number: int | None = None,
        **criteria: Any
    ) -> list[Self]:
        """
        Queries the database for a collection of <cls>
        business objects, returning a list of those that
        were retrieved.

        Parameters:
        -----------
        oids : UUID | str
            The unique object identifiers of the objects
            to retrieve and return.
        db_source_name : optional str
            The name of the table or view to execute the
            query against to retrieve the records for the
            objects to be created.
        page_size : optional int
            The number of records to query, and thus
            objects to return, as a "page" of results.
        page_number : optional int
            The number of the "page" of records to return.
        criteria : any
            The names and values to be used to generate
            the query, or (less ideally) to be used to
            filter results in code.
            May also be passed names to indicate a sort-
            order, of the form "sort_{field}"
            May also be passed names to indicate criteria
            and operations against any of the fields in
            the class' CRITERIA_FIELDS attribute, suffixed
            with any of the following operations:
            - _eq to use an equality comparison.
              Note that this suffix is optional; a field
              name with an "=" is equivalent to the
              _eq-suffixed name.
              For example:
                name='Dough'
              is equivalent to
                name_eq='Dough'
            - _neq  to use an inequality (!=) comparison.
            - _gt to use a greater-than (>) comparison.
            - _gte to use a greater-than-or-equal-to (>=)
              comparison.
            - _lt to use a less-than (>) comparison.
            - _lte to use a less-than-or-equal-to (<=)
              comparison.
            - _like to use a LIKE (LIKE '%some value%')
              evaluation.
            - _in to use a "membership" comparison with a
              list or tuple of specific values to match.
              For example:
                name_in=('John', 'Jane')
              or
                name_in=['John', 'Jane']
        """
        # Build the WHERE clause from **criteria,
        # including any oids values specified
        if oids:
            if len(oids) == 1:
                # Single oid
                criteria['oid'] = str(oids[0])
            else:
                # Multiple oids
                criteria['oid_in'] = [str(o) for o in oids]
        where, parameters = build_where_clause(
            criteria, cls.CRITERIA_FIELDS
        )

        # Build the ORDER BY clause from **criteria
        order_by = build_order_by_clause(
            criteria, cls.CRITERIA_FIELDS
        )

        # Build the LIMIT clause, if one is called for
        if page_size is not None \
                and page_number is not None:
            try:
                limit = build_limit_clause(
                    page_size, page_number
                )
            except AssertionError as error:
                raise ValueError(f'{error}') from error
        else:
            limit = ''

        # Generate the final SQL to execute
        final_sql = cls.GET_TEMPLATE.format(
            TABLE_NAME=db_source_name or cls.TABLE_NAME,
            WHERE=where, ORDER_BY=order_by,
            LIMIT=limit
        )

        # Get a connector, create a cursor, execute the
        # query (with parameters if any are supplied)
        connector = get_env_database_connector()
        with connector.cursor(dictionary=True) as cursor:
            if parameters:
                cursor.execute(final_sql, parameters)
            else:
                cursor.execute(final_sql)
            rows = cursor.fetchall()
        results = [
            cls.from_record(
                json.loads(row['object_state'])
            )
            for row in rows
        ]
        return results

    @classmethod
    def delete(
        cls,
        *oids: list[UUID | str],
        db_source_name: str | None = None,
    ) -> None:
        """
        Deletes records in the database specified by
        one or more oid values.

        Parameters:
        -----------
        oids : UUID | str
            The unique object identifiers of the object
            records to delete.
        """
        assert len(oids), \
            f'{cls.__name__}.delete must be ' \
            'provided specific oids to delete.'
        # Build the WHERE clause from **criteria,
        # including any oids values specified
        if oids:
            if len(oids) == 1:
                # Single oid
                criteria = {'oid': str(oids[0])}
            else:
                # Multiple oids
                criteria = {'oid_in': [str(o) for o in oids]}
        where, parameters = build_where_clause(
            criteria, cls.CRITERIA_FIELDS
        )
        final_sql = cls.DELETE_TEMPLATE.format(
            TABLE_NAME=db_source_name or cls.TABLE_NAME,
            WHERE=where
        )
        # Get the connector, create a cursor, execute the
        # query (with parameters if any are supplied)
        connector = get_env_database_connector()
        with connector.cursor() as cursor:
            if parameters:
                cursor.execute(final_sql, parameters)
            else:
                cursor.execute(final_sql)
        connector.commit()


# Module Concrete Classes

# Code to run if the module is executed directly
if __name__ == '__main__':

    pass
