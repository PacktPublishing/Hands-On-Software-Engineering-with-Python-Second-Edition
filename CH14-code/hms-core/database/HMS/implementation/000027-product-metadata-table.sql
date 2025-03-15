CREATE TABLE ProductMetadata (
    product_oid CHAR(36) NOT NULL
    COMMENT 'The unique identifier of the Product that this metadata key/value pair applies to.',
    category_name VARCHAR(32) NOT NULL
    COMMENT 'The category-name (key) of the metadata.',
    value VARCHAR(32) NOT NULL
    COMMENT 'The metadata value',
    PRIMARY KEY(product_oid, category_name, value)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci
COMMENT='Tracks metadata keys and values for specific products.'
;
