/**
 * This is the table, view, and functional permissions
 * set-up SQL for the HMS Service User account.
 * It must be run with credentials that allow granting
 * of permissions for tables, views, procedures and functions.
 *
 * This can be run safely if the user has already been created,
 * though it will report an error along the lines of:
 * Operation CREATE USER failed for '{MYSQL_SERVICE_USER}'@'%'
 */

-- Basic CRUD operations against tables
GRANT INSERT ON {MYSQL_DB}.* TO '{MYSQL_SERVICE_USER}'@'%';
GRANT SELECT ON {MYSQL_DB}.* TO '{MYSQL_SERVICE_USER}'@'%';
GRANT UPDATE ON {MYSQL_DB}.* TO '{MYSQL_SERVICE_USER}'@'%';
GRANT DELETE ON {MYSQL_DB}.* TO '{MYSQL_SERVICE_USER}'@'%';

-- Execution of stored routines
GRANT EXECUTE ON {MYSQL_DB}.* TO '{MYSQL_SERVICE_USER}'@'%';

-- Creation of temporaty tables (not needed at present)
-- GRANT CREATE TEMPORARY TABLES ON {MYSQL_DB}.* TO '{MYSQL_SERVICE_USER}'@'%';
