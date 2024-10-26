#!/usr/bin/env python3.11
"""
Provides concrete Artisan object-structure, derived from
the business_objects in hms.core.
"""
from __future__ import annotations

from hms.core.business_objects import BaseArtisan


class Artisan(BaseArtisan):
    """
    Represents an Artisan for those systems and endpoints with access to all Artisan data structure
    """  # noqa: E501
