#!/usr/bin/env python3.11
"""
A pure class-based approach to writing Business Objects.
"""

from __future__ import annotations

import abc
import json
import re

from typing import Optional

from typeguard import typechecked

EMAIL_PATTERN = re.compile(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
)


class IsJSONSerializable(metaclass=abc.ABCMeta):
    """
    Requires derived classes to implement a common
    json_safe_dict method to facilitate 
    """
    @abc.abstractmethod
    def json_safe_dict(self) -> dict:
        """
        Generates and returns a JSON-safe dict of the
        object's state-data.
        """
        raise NotImplementedError(
            f'{self.__class__.__name__}.json_dump has '
            'not been implemented, as required by '
            'IsJSONSerializable.'
        )


@typechecked
class BaseArtisan(
    IsJSONSerializable,
    metaclass=abc.ABCMeta
):
    """
    Provides baseline functionality, interface
    requirements, and type identity for objects that can
    represent an Artisan in the system.
    """

    def __init__(
        self,
        # Required parameters
        given_name: str, family_name: str,
        address: dict | Address,
        # Optional parameters
        email_address: Optional[str] = None,
        honorific: Optional[str] = None,
        suffix: Optional[str] = None,
    ):
        """
        Object initialization
        """
        self.honorific = honorific
        self.given_name = given_name
        self.family_name = family_name
        self.suffix = suffix
        self.address = Address(**address)
        self.email_address = email_address

    # Properties
    @property
    def address(self) -> Address:
        """
        Gets or sets the address of the Artisan
        that the instance represents
        """
        return self._address

    @address.setter
    def address(self, value: dict | Address) -> None:
        """
        Setter method for the address property
        """
        if isinstance(value, dict):
            value = Address(**value)
        self._address = value

    @property
    def email_address(self) -> str:
        """
        Gets or sets the email_address of the
        Artisan that the instance represents
        """
        return self._email_address

    @email_address.setter
    def email_address(self, value: str) -> None:
        """
        Setter method for the email_address property
        """
        # Validate of the incoming value
        if not EMAIL_PATTERN.match(value):
            raise ValueError(
                f'{self.__class__.__name__}.email was '
                f'passed "{value}", which did not match '
                f'the pattern "{EMAIL_PATTERN.pattern}".'
            )
        # If the value passes (there is a match), store it
        self._email_address = value

    @property
    def family_name(self) -> str:
        """
        Gets or sets the family_name of the
        Artisan that the instance represents
        """
        return self._family_name

    @family_name.setter
    def family_name(self, value: str) -> None:
        """
        Setter method for the family_name property
        """
        # TODO: Validate of the incoming value
        self._family_name = value

    @property
    def given_name(self) -> str:
        """
        Gets or sets the given_name of the
        Artisan that the instance represents
        """
        return self._given_name

    @given_name.setter
    def given_name(self, value: str) -> None:
        """
        Setter method for the given_name property
        """
        # Pre-process the value to remove leading
        # and trailing white space
        value = value.strip()
        # Validate the length of the value string
        if len(value) < 2:
            raise ValueError(
                f'{self.__class__.__name__}.given_name '
                'must be at least two characters long'
            )
        # If this point is reached, the value is valid,
        # so store it
        self._given_name = value

    @property
    def honorific(self) -> Optional[str]:
        """
        Gets or sets the honorific of the
        Artisan that the instance represents
        """
        return getattr(self, '_honorific', None)

    @honorific.setter
    def honorific(
        self, value: Optional[str] = None
    ) -> None:
        """
        Setter method for the honorific property
        """
        # If the value is None, set it and be done
        # with it
        if value is None:
            self._honorific = value
            return
        # Otherwise, pre-process the value to remove
        # leading and trailing white space
        value = value.strip()
        # If what's left is an empty string, we
        # can also set it to None, then exit
        if not len(value):
            self._honorific = None
            return
        # Otherwise, validate the length of the value
        if len(value) < 2 or len(value) > 7:
            raise ValueError(
                f'{self.__class__.__name__}.given_name '
                'must be two to seven characters long'
            )
        # If this point is reached, the value is valid,
        # so store it
        self._honorific = value

    @property
    def suffix(self) -> Optional[str]:
        """
        Gets or sets the suffix of the Artisan
        that the instance represents
        """
        return self._suffix

    @suffix.setter
    def suffix(self, value: Optional[str] = None) -> None:
        """
        Setter method for the suffix property
        """
        # TODO: Validate of the incoming value
        self._suffix = value

    def json_safe_dict(self) -> dict:
        return {
            'address': self.address.json_safe_dict(),
            'email_address': self.email_address,
            'family_name': self.family_name,
            'given_name': self.given_name,
            'honorific': self.honorific,
            'suffix': self.suffix,
        }


@typechecked
class Address(IsJSONSerializable):
    """
    Represents a physical address, where mail could be
    sent.
    """

    def __init__(
        self,
        # Required parameters
        street_address: str, city: str, region: str,
        postal_code: str,
        # Optional parameters
        building_address: Optional[str] = None,
        country: Optional[str] = None,
    ):
        """
        Object initialization
        """
        # Set instance state from parameters
        self.street_address = street_address
        self.building_address = building_address
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.country = country

    # Properties
    @property
    def street_address(self) -> str:
        """
        Gets or sets the street address portion
        of the address that the instance represents.
        """
        return self._street_address

    @street_address.setter
    def street_address(self, value: str) -> None:
        """
        Setter method for the street_address property
        """
        # TODO: Validate of the incoming value
        self._street_address = value

    @property
    def building_address(self) -> Optional[str]:
        """
        Gets or sets the "building address"
        portion of the address that the instance
        represents: An apartment or suite number, for
        example
        """
        return self._building_address

    @building_address.setter
    def building_address(self, value: Optional[str]) -> None:
        """
        Setter method for the building_address property
        """
        # TODO: Validate of the incoming value
        self._building_address = value

    @property
    def city(self) -> str:
        """
        Gets or sets the city portion of the
        address that the instance represents.
        """
        return self._city

    @city.setter
    def city(self, value: str) -> None:
        """
        Setter method for the city property
        """
        # TODO: Validate of the incoming value
        self._city = value

    @property
    def region(self) -> str:
        """
        Gets or sets the region portion of the
        address that the instance represents, for example
        a state in the US, or a province in Canada.
        """
        return self._region

    @region.setter
    def region(self, value: str) -> None:
        """
        Setter method for the region property
        """
        # TODO: Validate of the incoming value
        self._region = value

    @property
    def postal_code(self) -> str:
        """
        Gets or sets the postal code portion of
        the address that the instance represents, for
        example a ZIP Code in the US.
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value: str) -> None:
        """
        Setter method for the postal_code property
        """
        # TODO: Validate of the incoming value
        self._postal_code = value

    @property
    def country(self) -> Optional[str]:
        """
        Gets or sets the country portion of the
        address that the instance represents.
        """
        return self._country

    @country.setter
    def country(self, value: Optional[str]) -> None:
        """
        Setter method for the country property
        """
        # TODO: Validate of the incoming value
        self._country = value

    def json_safe_dict(self) -> dict:
        return {
            'building_address': self.building_address,
            'city': self.city,
            'country': self.country,
            'postal_code': self.postal_code,
            'region': self.region,
            'street_address': self.street_address,
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
    print(json.dumps(instance.json_safe_dict(), indent=4))
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
