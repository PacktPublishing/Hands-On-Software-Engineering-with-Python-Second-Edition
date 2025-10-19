"""
Module: data_object.py
Description:
    This module provides a foundational data model class for HMS objects using Pydantic.
    The BaseDataObject defines fields typically present in persistent records and
    includes metadata like creation/modification timestamps, object status flags,
    and a UUID-based primary key.

    It also provides a scaffold for CRUD operations such as retrieval with filtering,
    pagination, and criteria-based selection.
"""

from typing import List, Optional, Union, Dict, Any, Tuple
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class BaseDataObject(BaseModel):
    oid: UUID = Field(
        default_factory=uuid4,
        description="The unique object identifier (UUID) for this record.",
        examples=["123e4567-e89b-12d3-a456-426614174000", "987e6543-e21b-45d6-a321-123456789abc"]
    )
    created: datetime = Field(
        default_factory=datetime.utcnow,
        description="UTC datetime when the object was created.",
        examples=["2023-01-01T12:00:00Z", "2024-12-25T08:30:45Z"]
    )
    modified: datetime = Field(
        default_factory=datetime.utcnow,
        description="UTC datetime when the object was last modified.",
        examples=["2023-01-01T12:00:00Z", "2024-12-25T08:30:45Z"]
    )
    is_active: bool = Field(
        default=False,
        description="Indicates whether the record is currently active.",
        examples=[True, False]
    )
    is_deleted: bool = Field(
        default=False,
        description="Indicates whether the record has been marked as deleted.",
        examples=[True, False]
    )

    @classmethod
    def get(
        cls,
        cursor,
        oids: Optional[List[Union[str, UUID]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        criteria: Optional[Dict[str, Any]] = None
    ) -> Tuple[str, List[Any]]:
        """
        Retrieves records based on object IDs, optional criteria, and pagination.

        :param cursor: A DB-API 2.0 compliant cursor object for executing queries.
        :param oids: List of UUIDs or strings representing object IDs.
        :param limit: Optional maximum number of records.
        :param offset: Optional record offset for pagination.
        :param criteria: Dictionary of additional selection filters.
        :return: Executed SQL query string and list of parameter values.
        """
        query = "SELECT * FROM data_objects WHERE 1=1"
        params = []

        if oids:
            placeholders = ', '.join(['%s'] * len(oids))
            query += f" AND oid IN ({placeholders})"
            params.extend([str(oid) for oid in oids])

        if criteria:
            for key, value in criteria.items():
                query += f" AND {key} = %s"
                params.append(value)

        if limit is not None:
            query += " LIMIT %s"
            params.append(limit)

        if offset is not None:
            query += " OFFSET %s"
            params.append(offset)

        cursor.execute(query, params)
        return query, params

    @classmethod
    def delete(cls, cursor, oids: List[Union[str, UUID]]) -> Tuple[str, List[Any]]:
        """
        Deletes (or soft-deletes) objects based on OID list.

        :param cursor: A DB-API 2.0 compliant cursor object for executing queries.
        :param oids: List of UUIDs or strings representing object IDs.
        :return: Executed SQL query string and list of parameter values.
        """
        query = "DELETE FROM data_objects WHERE oid IN ({})".format(
            ', '.join(['%s'] * len(oids))
        )
        params = [str(oid) for oid in oids]
        cursor.execute(query, params)
        return query, params

    def save(self, cursor) -> Tuple[str, List[Any]]:
        """
        Saves the current object to the database. Performs an INSERT.

        :param cursor: A DB-API 2.0 compliant cursor object for executing queries.
        :return: Executed SQL query string and list of parameter values.
        """
        self.modified = datetime.utcnow()
        query = """
        INSERT INTO data_objects (oid, created, modified, is_active, is_deleted)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (oid) DO UPDATE SET
            modified = EXCLUDED.modified,
            is_active = EXCLUDED.is_active,
            is_deleted = EXCLUDED.is_deleted
        """
        params = [
            str(self.oid),
            self.created.isoformat(),
            self.modified.isoformat(),
            self.is_active,
            self.is_deleted
        ]
        cursor.execute(query, params)
        return query.strip(), params
