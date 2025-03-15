# Database Implementation

The SQL scripts in this directory should be executed with the local developer account that was created when the [database set-up process](../../DATABASE-SETUP.md) was executed. Access to the local database using that user account can be verified by executing

```shell
mysql -D HMS_DEV -p
```

(This will will prompt you for a password; use your **local developer password**.)

If any of the following errors/results are returned, your local database has not been set up completely, and that should be executed first:

- `ERROR 1049 (42000): Unknown database 'HMS_DEV'`
- `ERROR 1045 (28000): Access denied for user '{username}'@'localhost' (using password: YES)`

## How to create and use these files

These files are intended to capture the **entire sequence** of changes made to any instances of `HMS_DEV` database, both local developer **and production** instances, in such a way that they can be applied, in sequence, to replicate **all** changes made over time in any given environment. To that end, it is important that:

- Every file-name starts with a **sequence number** (six digits)
- Every SQL statement within every file should be written with the expectation that the file will be executed as part of a scripted batch-process.

The entire collection of SQL files can be run against a local database with [the `apply-sql.py` script](apply-sql.py) in this directory. It will prompt you for a password in order to create a backup of the local database first, saving those as `.backup` files in [the `backups` directory](../backups). They can also be run with the `mysql` CLI, with commands like this example:

```shell
mysql -D HMS_DEV -p < 000000-initial-state.sql
```

They can also be run from within a MySQL session, using the `SOURCE` statement, like this:

```sql
SOURCE 000000-initial-state.sql
```

**Note:** The `SOURCE` statement must either be executed in a MySQL session that was started in this directory, or the absolute path to the source file must be specified.

## Periodic maintenance

From time to time, it will be beneficial to "squash" the change-set 
