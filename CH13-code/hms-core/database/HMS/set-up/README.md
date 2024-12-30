# Database set-up

The SQL scripts in this directory need to be executed with sufficient permissions to create the database, the application user, and to grant permissions to your developer user-name. The `root` account that was created with your MySQL installation will have those permissions, and these scripts have been tested using that account.

Any of these commands that start with `mysql -u root -p` will prompt you for a **root** password.

1. Create the database with

```shell
mysql -u root -p < 001-create-application-database.sql
```

2. Create the service user database account with

```shell
mysql -u root -p < 002-create-application-user.sql
```

3. Grant the basic permissions for the service user database with

```shell
mysql -u root -p < 003-grant-application-user-permissions.sql
```

4. Set up local administrative permissions for your user account

If you don't know the default local user-name that your MySQL installation will look for, it can be determined by running this shell command:

```shell
mysql -D HMS_DEV -p
```
If it returns an `Access denied for user `'username'@'localhost'` error, the `username` it specifies is the `{MYSQL_USER}` value that needs to be specified in the SQL below.

If your MySQL installation is completely new, log in to it with your root credentials using:

```shell
mysql -u root -p
```

and execute this SQL to create your local developer user account:

```sql
CREATE USER '{MYSQL_USER}'@'%'
IDENTIFIED BY 'your-local-mysql-password';
```

then set up your development permissions with the following SQL:

```sql
GRANT ALTER ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT CREATE ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT CREATE VIEW ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT DELETE ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT DROP ON HMS_DEV.* TO '{MYSQL_USER}'@'%' WITH GRANT OPTION;
GRANT INDEX ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT INSERT ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT REFERENCES ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT SELECT ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT SHOW VIEW ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT TRIGGER ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT UPDATE ON HMS_DEV.* TO '{MYSQL_USER}'@'%' WITH GRANT OPTION;
GRANT LOCK TABLES ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT EXECUTE ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT CREATE TEMPORARY TABLES ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT CREATE ROUTINE ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
GRANT ALTER ROUTINE ON HMS_DEV.* TO '{MYSQL_USER}'@'%';
```

Once all of this is complete, you should be able to log in to mysql from a terminal with

```shell
mysql -D HMS_DEV -p
```

You will need to provide your **non-root** password.

At this point, assuming that these scripts were run to create a new database instance from scratch, running

```sql
show tables;
```

should succeed, returning an `Empty set` result.
