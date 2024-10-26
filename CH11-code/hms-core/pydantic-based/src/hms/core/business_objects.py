#!/usr/bin/env python3.11
"""
A Pydantic-based approach to writing Business Objects.
"""
from __future__ import annotations

import abc
import json
import os

from pathlib import Path
from typing import Optional

import yaml

from pydantic import BaseModel, Field


class Address(BaseModel):
    """
    Represents a physical address, where mail could be sent.
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
        description='The phone number address for the Artisan '
        'that the instance represents',
        pattern=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',
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


schema_file = Path(__file__).parent / __file__.split(os.sep)[-1].replace('py', 'schema.json')
schema_items = {'schemas':{}}
for cls in (Address, BaseArtisan):
    print(f'== {cls.__name__} schema '.ljust(56, '='))
    schema = cls.model_json_schema()
    if '$defs' in schema:
        del schema['$defs']
    schema_items['schemas'][cls.__name__] = schema
    # ~ print(yaml.dump(schema, default_flow_style=False))
schema_file.write_text(json.dumps(schema_items, indent=4).replace('#/$defs/', '#/schemas/'))

import yaml
schema_file = Path(__file__).parent / __file__.split(os.sep)[-1].replace('py', 'oas.yaml')
schemas = schema_items['schemas']
for name, item in schemas.items():
    properties = item.get('properties')
    if properties:
        for prop_name, prop in properties.items():
            print(f'{prop_name}: {prop}')
            if 'examples' in prop:
                prop['example'] = prop['examples'][0]
                del prop['examples']
oas_schema = {
    'openapi': '3.0.3',
    'info': {
        'title': f'Example components schemas from {__file__.split(os.sep)[-1]}',
    },
    'components': schema_items
}
schema_file.write_text(yaml.dump(oas_schema, default_flow_style=False).replace('#/$defs/', '#/components/schemas/'))

print('== Examples '.ljust(56, '='))

example_artisan = {
    # Omitting the optional honorific, suffix,
    # and phone values
    "given_name": "John",
    "family_name": "Smith",
    "email_address": "john.smith@test.com",
    "phone": "303-555-1212",
    "address": {
        # Omitting the optional building_address
        # and country values
        "street_address": "1234 Main Street",
        "city": "Springfield",
        "region": "Some Place",
        "postal_code": "98765-4321"
    }
}

try:
    instance = BaseArtisan(**example_artisan)
    print('Valid Artisan data-structure:')
    print(json.dumps(instance.model_dump(mode='json'), indent=4))
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

try:
    instance.given_name = None
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan['given_name'] = None

try:
    instance = BaseArtisan(**example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    # Expected error given_name must be a string value
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan['given_name'] = 'John'
example_artisan['address']['street_address'] = None

try:
    instance = BaseArtisan(**example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    # Expected error given_name must be a string value
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan['address']\
    ['street_address'] = '1234 Main Street'
example_artisan['additional_field'] = True

try:
    instance = BaseArtisan(**example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

del example_artisan['additional_field']
example_artisan['email_address'] = 'not an email address'

try:
    instance = BaseArtisan(**example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan = {}

try:
    instance = BaseArtisan(**example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

