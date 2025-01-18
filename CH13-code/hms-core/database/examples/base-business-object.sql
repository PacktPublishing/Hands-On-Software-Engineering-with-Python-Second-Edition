CREATE TABLE BaseBusinessObject (
    oid CHAR(36) NOT NULL PRIMARY KEY
    COMMENT 'The unique identifier of the record; a UUID value (for example b279fda6-eafc-40e5-b8c7-415ed864acf7).',
    is_active TINYINT(1) DEFAULT 1 NOT NULL
    COMMENT 'Flag indicating whether the object state-data is active (1/True) or not (0/False)',
    is_deleted tinyint(1) DEFAULT 0 NOT NULL
    COMMENT 'Flag indicating whether the object state-data is considered "deleted," and thus not accessible (1/True) or not (0/False)',
    created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
    COMMENT 'The UTC date/time that the record was originally created.',
    modified DATETIME ON UPDATE CURRENT_TIMESTAMP NULL
    COMMENT 'The UTC date/time that the record was last modified.'
    /**
      * TODO: Add a JSON field for the JSON state of the object,
      * named after the object type. For example:
        {business_object}_data JSON DEFAULT 'null' NOT NULL
        COMMENT 'The state data of the {BusinessObject} object, serialized to JSON.',
      *
      * Also be sure to add a comma after the modified field's COMMENT. ;-)
      */
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci
COMMENT='A reference table, showing common fields and their definitions for other tables that will store business object state-data.'
;
