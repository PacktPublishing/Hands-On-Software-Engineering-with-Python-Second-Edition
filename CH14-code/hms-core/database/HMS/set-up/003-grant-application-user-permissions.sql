/**
 * This is the table, view, and functional permissions
 * set-up SQL for the HMS Service User account.
 * It must be run with credentials that allow granting
 * of permissions for tables, views, procedures and functions.
 *
 * This can be run safely if the user has already been created,
 * though it will report an error along the lines of:
 * Operation CREATE USER failed for 'hms-service-user'@'%'
 */

-- Basic CRUD operations against tables
GRANT INSERT ON HMS_DEV.* TO 'hms-service-user'@'%';
GRANT SELECT ON HMS_DEV.* TO 'hms-service-user'@'%';
GRANT UPDATE ON HMS_DEV.* TO 'hms-service-user'@'%';
GRANT DELETE ON HMS_DEV.* TO 'hms-service-user'@'%';

-- Execution of stored routines
GRANT EXECUTE ON HMS_DEV.* TO 'hms-service-user'@'%';

-- Creation of temporaty tables (not needed at present)
-- GRANT CREATE TEMPORARY TABLES ON HMS_DEV.* TO 'hms-service-user'@'%';
