#!/usr/bin/env python3.11
"""
Provides Business Objects definitions, implemented using
Pydantic.
"""
from __future__ import annotations

import abc

from typing import Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    """
    Represents a physical addresaas, where mail could be sent.
    """  # noqa: E501

    street_address: str = Field(
        title='Street Address',
        description='The street address portion of the '
        'address that the instance represents. May also '
        'contain a post office box',
        examples=[
            '1234 Main Street',
            'PO Box 1234'
        ]
    )
    building_address: Optional[str] = Field(
        title='Building Address', default=None,
        description='The "building address" (an '
        'apartment number, suite, etc.) portion of the '
        'address that the instance represents',
        examples=[
            None,
            'Apt. 56', 'Suite 321',
        ]
    )
    city: str = Field(
        title='City',
        description='The city portion of the address '
        'that the instance represents',
        examples=[
            'Springfield',
        ]
    )
    region: str = Field(
        title='Region',
        description='The region portion (a state in the '
        'US, or a province in Canada, for example) of '
        'the address that the instance represents',
        examples=[
            'Some Place',
        ]
    )
    postal_code: str = Field(
        title='Postal Code',
        description='The postal code portion (a ZIP Code '
        'in the US, for example) of the address that the '
        'instance represents',
        examples=[
            '12345',
            '12345-6789',
            'SW1A 2AA',  # British
            'M5V 3L9',   # Canadian
        ]
    )
    country: Optional[str] = Field(
        title='Country', default=None,
        description='The country portion of the address '
        'that the instance represents. Typically '
        'omitted, indicating that the address is "local" '
        'to the country of origin.',
        examples=[
            None,
            'United States', 'Great Britain', 'Canada',
        ]
    )


class BaseArtisan(BaseModel, metaclass=abc.ABCMeta):
    """
    Provides baseline functionality, interface requirements, and type identity for objects that can represent an Artisan in the system.
    """  # noqa: E501

    honorific: Optional[str] = Field(
        title='Honorific', default=None,
        description='The honorific of the Artisan that '
        'the instance represents',
        min_length=2,
        max_length=7,
        examples=[
            None,
            'Mr.', 'Ms.', 'Mrs.', 'Dr.'
        ]
    )
    given_name: str = Field(
        title='Given Name',
        description='The given name of the artisan that '
        'the instance represents',
        min_length=2,
        examples=[
            'John',
            'Jane',
        ]
    )
    family_name: str = Field(
        title='Family Name',
        description='The family name of the artisan that '
        'the instance represents',
        min_length=2,
        examples=[
            'Smith',
            'Jones',
        ]
    )
    suffix: Optional[str] = Field(
        title='Suffix', default=None,
        description='The name suffix of the Artisan that '
        'the instance represents',
        min_length=2,
        max_length=7,
        examples=[
            None,
            'Jr.', 'III'
        ]
    )
    address: Address = Field(
        title='Mailing Address',
        description='The mailing address for the Artisan '
        'that the instance represents'
    )
    phone: str = Field(
        title='Phone Number',
        description='The phone number address for the '
        'Artisan that the instance represents',
        pattern=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]'
        r'\d{3}[\s.-]\d{4}$',
        examples=[
            '303-555-1212',
            '(303) 555-1212',
        ]
    )
    email_address: str = Field(
        title='Email Address',
        description='The email address for the Artisan '
        'that the instance represents',
        pattern=r'^[a-zA-Z0-9\._%+\-]+'
        r'@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,}$',
        examples=[
            'jsmith@gmail.com',
        ]
    )
