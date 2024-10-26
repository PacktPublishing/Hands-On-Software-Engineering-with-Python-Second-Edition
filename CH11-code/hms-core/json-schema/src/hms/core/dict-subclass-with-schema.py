#!/usr/bin/env python3.11
"""
A dictionary-based approach to writing Business Objects,
using fastjsonschema to validate structure.
"""

import json

import fastjsonschema

class SchemaBoundDict(dict):
    """
    An Abstract Base Class that also derives from Python's
    built-in dict, that requires a JSON schema
    """

    OBJECT_SCHEMA = None
    object_validator = None

    def __init__(self, *args, **kwargs):
        """
        Object initialization

        Checks for the class OBJECT_SCHEMA class attribute,
        and creates the object_validator object before 
        initializing the instance as normal for a dict.

        Raises:
        -------
        AssertionError:
            If the class does not define an OBJECT_SCHEMA
            dictionary.
        RuntimeError:
            If the object_validator cannot be created for
            any reason.
        """
        assert isinstance(
            self.__class__.OBJECT_SCHEMA, dict
        ), f'{self.__class__.__name__}.OBJECT_SCHEMA ' \
            'is not defined as a JSON Schema dict.'
        if self.__class__.object_validator is None:
            try:
                self.__class__.object_validator = fastjsonschema.compile(
                    self.__class__.OBJECT_SCHEMA
                )
            except Exception as error:
                raise RuntimeError(
                    f'{error.__class__.__name__}: Could '
                    f'not create {self.__class__.__name__}'
                    '.object_validator'
                ) from error
        dict.__init__(self, *args, **kwargs)
        self.object_validator(self)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        self.object_validator(self)


class BaseArtisan(SchemaBoundDict):
    """
    A schema-bound dictionary providing baseline
    functionality, interface requirements, type identity,
    and schema-controlled data structure constaints and
    validation for objects that represent an Artisan in
    the system.
    """
    OBJECT_SCHEMA = {
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


try:
    instance = BaseArtisan(**example_artisan)
    print('Valid Artisan data-structure:')
    print(json.dumps(instance, indent=4))
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

try:
    instance['given_name'] = None
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan['given_name'] = None

try:
    instance = BaseArtisan(**example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(instance, indent=4))
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
    print(json.dumps(instance, indent=4))
except Exception as error:
    # Expected error given_name must be a string value
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan['address']['street_address'] = '1234 Main Street'
example_artisan['additional_field'] = True

try:
    instance = BaseArtisan(**example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(instance, indent=4))
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
    print(json.dumps(instance, indent=4))
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )

example_artisan = {}

try:
    instance = BaseArtisan(**example_artisan)
    print('This example_artisan should raise an error:')
    print(json.dumps(instance, indent=4))
except Exception as error:
    print(
        'Expected error: '
        f'{error.__class__.__name__}: {error}'
    )
