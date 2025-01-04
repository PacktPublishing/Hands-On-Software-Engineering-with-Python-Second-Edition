#!/usr/bin/env python3.11
"""
Provides classes and functionality for defining and
working with businbess-object classes whose state-data
is persisted in a back-end data-store.
"""
from __future__ import annotations

# Built-In Imports
import abc
import os

from datetime import datetime
from functools import cache
from typing import Any
from uuid import UUID, uuid4

# Third-Party Imports
import mysql.connector

from pydantic import BaseModel, Field

from mysql.connector.connection_cext import CMySQLConnection

# Path Manipulations (avoid these!) and "Local" Imports

# Module "Constants" and Other Attributes

# Module Custom Exceptions


# Module Functions
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
        examples=[True, False],
        default=False
    )
    is_deleted: bool = Field(
        title='Is Deleted',
        description='Flag indicating whether the object '
        'is "deleted" (pending an **actual** deletion '
        'later, perhaps).',
        examples=[True, False],
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


# Module Concrete Classes


# Code to run if the module is executed directly
if __name__ == '__main__':

    with get_env_database_connector() as db:
        with db.cursor() as cursor:
            cursor.execute('SHOW TABLES;')
            print(
                'SHOW TABLES results: '
                f'{cursor.fetchall()}'
            )
