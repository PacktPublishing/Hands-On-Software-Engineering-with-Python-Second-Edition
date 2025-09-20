/**
 * This is the set-up SQL for the HMS Service User account.
 * It must be run with credentials that allow user creation.
 * The root user created when MySQL was install WILL have
 * the necessary permissions, so it's probably easiest to
 * run this using that account.
 *
 * This can be run safely if the user has already been created,
 * though it will report an error along the lines of:
 * Operation CREATE USER failed for 'hms-service-user'@'%'
 */

CREATE USER '{MYSQL_SERVICE_USER}'@'%'
    IDENTIFIED BY '{MYSQL_SERVICE_PASS}'
;
