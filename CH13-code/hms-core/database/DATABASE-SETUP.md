# Setting up a development database

[TOC]

## Prerequisites

* Make sure you have a working MySQL installation.
  - If you don't follow the instructions in the [MySQL Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/) for your operating system.
  - ***Be sure to keep track of the `root` credentials for your installation***: they will be needed later to set up the local database user.
  - If you want a GUI to interact with the database:
    - The [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) is available for several operating systems (but *not* all that MySQL can run under, unfortunately).
    - The [DBeaver Community](https://dbeaver.io/) tool may be a viable alternative as well, especially for operating systems that lack support for the MySQL Workbench. **Note:** DBeaver is an Eclipse-derived program, and may be a resource hog!
* If you haven't already, make a copy of the `template.env` file in `.env`. This file will eventually store the various MySQL parameters needed by the project code:
  - `MYSQL_HOST` will be the host-name used to connect to the database; Using `localhost` is known to work for Linux installations.
  - `MYSQL_PORT` is the port that the MySQL service will be accessed at. The default port for MySQL is `3306`, unless it is configured otherwise.
  - `MYSQL_DB` is the name of the database that will be used. The `template.env` file assumes that the local database name will be `HMS_DEV`, as does the user set-up SQL below.
  - `MYSQL_USER` will be the application user-name used to connect to the database. The `template.env` file has a placeholder value that should be replaced: `SYNC WITH YOUR ENV FILE`. Your local application user-name does **not** need to be the same as the equivalent in the production systems, so it can be set as you see fit, but it should have a value, even if it is not a secure one.
  - `MYSQL_PASS` will be the password used for the application user-name to connect to the database. The `template.env` file has a placeholder value that should be replaced: `SYNC WITH YOUR ENV FILE`. Your local application password will almost certainly **not** be the same as the equivalent in the production systems, so it can be set as you see fit, but it should have a value, even if it is not a secure one.

## Local Database Creation

Using the `root` credentials for your MySQL installation, create a local database.
- See the [set-up README file](HMS/set-up/README.md) for details on this process.
- The set-up will also grant permissions for your local account to act as a database administrator for the local database.
* Grant all of the *Developer Permissions* noted below — these will be used during development to allow you, the developer, to work with the database as needed.

