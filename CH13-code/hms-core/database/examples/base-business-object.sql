CREATE TABLE BaseBusinessObject (
    oid CHAR(36) NOT NULL
    COMMENT 'The unique identifier of the record; a UUID value (for example b279fda6-eafc-40e5-b8c7-415ed864acf7).',
    is_active TINYINT(1) DEFAULT 1 NOT NULL
    COMMENT 'Flag indicating whether the object state-data is active (1/True) or not (0/False)',
    is_deleted tinyint(1) DEFAULT 0 NOT NULL
    COMMENT 'Flag indicating whether the object state-data is considered "deleted," and thus not accessible (1/True) or not (0/False)',
    created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
    COMMENT 'The UTC date/time that the record was originally created.',
    modified DATETIME ON UPDATE CURRENT_TIMESTAMP NULL
    COMMENT 'The UTC date/time that the record was last modified.',
    object_data json NOT NULL
    COMMENT 'The JSON representation of the state-data for the object.',
    CONSTRAINT BaseBusinessObject_PK PRIMARY KEY (oid)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci
COMMENT='A reference table, showing common fields and their definitions for other tables that will store business object state-data.'
;
