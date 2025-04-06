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

from typing import List, Optional, Union, Dict, Any
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

    def get(
        self,
        oids: Optional[List[Union[str, UUID]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        criteria: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Simulates retrieval of records with filtering and pagination.

        :param oids: List of object IDs to retrieve.
        :param limit: Max number of records to retrieve.
        :param offset: Number of records to skip.
        :param criteria: Dictionary of filtering criteria (e.g. {"is_active": True}).
        :return: Simulated SQL or query string.
        """
        query_parts = ["SELECT * FROM data_objects WHERE 1=1"]

        if oids:
            formatted_ids = ", ".join(f"'{str(oid)}'" for oid in oids)
            query_parts.append(f"AND oid IN ({formatted_ids})")

        if criteria:
            for key, value in criteria.items():
                if isinstance(value, str):
                    value = f"'{value}'"
                query_parts.append(f"AND {key} = {value}")

        if limit is not None:
            query_parts.append(f"LIMIT {limit}")
        if offset is not None:
            query_parts.append(f"OFFSET {offset}")

        return " ".join(query_parts)
