#!/usr/bin/env python3.11
"""
Provides classes and functionality for defining and
working with businbess-object classes whose state-data
is persisted in a back-end data-store.
"""
from __future__ import annotations

# Built-In Imports
import os

from functools import cache

# Third-Party Imports
import mysql.connector

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
