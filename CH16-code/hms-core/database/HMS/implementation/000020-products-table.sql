CREATE TABLE Products (
    oid CHAR(36) NOT NULL PRIMARY KEY
    COMMENT 'The unique identifier of the record; a UUID value (for example b279fda6-eafc-40e5-b8c7-415ed864acf7).',
    is_active TINYINT(1) DEFAULT 0 NOT NULL
    COMMENT 'Flag indicating whether the object state-data is active (1/True) or not (0/False)',
    is_deleted TINYINT(1) DEFAULT 0 NOT NULL
    COMMENT 'Flag indicating whether the object state-data is considered "deleted," and thus not accessible (1/True) or not (0/False)',
    created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
    COMMENT 'The UTC date/time that the record was originally created.',
    modified DATETIME ON UPDATE CURRENT_TIMESTAMP NULL
    COMMENT 'The UTC date/time that the record was last modified.',
    artisan_oid CHAR(36) NOT NULL
    COMMENT 'The unique identifier of the Artisan that this record relates to/is owned by; a UUID value (for example b279fda6-eafc-40e5-b8c7-415ed864acf7).',
    object_state JSON NOT NULL
    COMMENT 'The JSON-serialized state-data of the object this record represents'
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci
COMMENT='Tracks Products in the system'
;
