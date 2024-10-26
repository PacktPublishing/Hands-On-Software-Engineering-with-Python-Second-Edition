#!/usr/bin/env python3.11
"""
A dictionary-based approach to writing Business Objects,
using fastjsonschema to validate structure.
"""

ARTISAN_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "honorific": {
            "type": "string",
            "minLength": 2,
            "maxLength": 7
        },
        "given_name": {
            "type": "string",
            "minLength": 2
        },
        "family_name": {
            "type": "string",
            "minLength": 2
        },
        "suffix": {
            "type": "string",
            "minLength": 2,
            "maxLength": 7
        },
        "email_address": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
        },
        "phone": {
            "type": "string",
            "pattern": "^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]\\d{3}[\\s.-]\\d{4}$"
        },
        "address": {
            "type": "object",
            "properties": {
                "street_address": {
                    "type": "string"
                },
                "building_address": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "region": {
                    "type": "string"
                },
                "postal_code": {
                    "type": "string"
                },
                "country": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "street_address",
                "city",
                "region",
                "postal_code"
            ]
        }
    },
    "additionalProperties": False,
    "required": [
        "given_name",
        "family_name",
        "email_address",
        "address"
    ]
}

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
        "postal_code": "98765-4321"
    }
}

import json

import fastjsonschema

artisan_validator = fastjsonschema.compile(ARTISAN_SCHEMA)

try:
    artisan_validator(example_artisan)
    print('Valid Artisan data-structure:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    print(error)

example_artisan['given_name'] = None

try:
    artisan_validator(example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    # Expected error given_name must be a string value
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan['given_name'] = 'John'
example_artisan['additional_field'] = True

try:
    artisan_validator(example_artisan)
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
    artisan_validator(example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan = {}

try:
    artisan_validator(example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(example_artisan, indent=4))
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )
