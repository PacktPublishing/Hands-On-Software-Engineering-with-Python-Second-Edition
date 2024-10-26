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

from pydantic import BaseModel


class Address(BaseModel):
    """
    Represents a physical address, where mail could be sent.
    """  # noqa: E501

    street_address: str
    building_address: Optional[str] = None
    city: str
    region: str
    postal_code: str
    country: Optional[str] = None


class BaseArtisan(BaseModel, metaclass=abc.ABCMeta):
    """
    Provides baseline functionality, interface requirements, and type identity for objects that can represent an Artisan in the system.
    """  # noqa: E501

    honorific: Optional[str] = None
    given_name: str
    family_name: str
    suffix: Optional[str] = None
    address: Address
    email_address: str


schema_file = Path(__file__).parent / __file__.split(os.sep)[-1].replace('py', 'schema.json')
schema_items = {'schemas':{}}
for cls in (Address, BaseArtisan):
    print(f'== {cls.__name__} schema '.ljust(56, '='))
    schema = cls.model_json_schema()
    if '$defs' in schema:
        del schema['$defs']
    schema_items['schemas'][cls.__name__] = schema
    print(yaml.dump(schema, default_flow_style=False))
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
    "address": {
        # Omitting the optional building_address
        # and country values
        "street_address": "1234 Main Street",
        "city": "Springfield",
        "region": "Some Place",
        "postal_code": "98765-4321",
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

