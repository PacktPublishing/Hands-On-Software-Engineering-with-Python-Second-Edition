/**
 * This is the set-up SQL for the HMS Service database.
 * It must be run with credentials that allow database creation.
 * The root user created when MySQL was install WILL have
 * the necessary permissions, so it's probably easiest to
 * run this using that account.
 *
 * This can be run safely if the user has already been created,
 * though it will report an error along the lines of:
 * Can't create database 'HMS_DEV'; database exists
 */

CREATE DATABASE HMS_DEV
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci
;
