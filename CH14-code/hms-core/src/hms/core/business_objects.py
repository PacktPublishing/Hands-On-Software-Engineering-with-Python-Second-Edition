#!/usr/bin/env python3.11
"""
"""
from __future__ import annotations

# Built-In Imports
import itertools

from decimal import Decimal
from random import shuffle
from typing import Any, ClassVar, Optional
from uuid import UUID

# Third-Party Imports
from pydantic import (
    # Model-related items
    BaseModel, Field,
    # Specific formats used in models
    EmailStr, NameEmail, HttpUrl,
    # Errors
    PydanticUserError
)

# Path Manipulations (avoid these!) and "Local" Imports
from hms.core.data_objects import BaseDataObject

# Module "Constants" and Other Attributes

# Module Custom Exceptions


# Module Functions
def get_examples(
    cls: BaseModel,
    *,
    randomize: bool = False,
    max_items: int | None = None
) -> list[dict[str, Any]]:
    """
    Returns a list of example instances of data for the
    supplied BaseModel class.

    cls : BaseModel-derived class
        The BaseModel class to generate examples for
    randomize : bool
        Whether to randomize those examples before
        returning them. Randomizing will lead to different
        examples for JSON schemas and OAS definitions
        that derive from those every time they are
        published, which may not be desired behavior.
    max_items : int
        The maximum number of examples to return

    Note:
    -----
    This function uses itertools.product to generate a
    Cartesian set of all possible example values. Model
    classes with large numbers of fields and/or large
    numbers of example values will take correspondigly
    longer times to generate. It is recommended that no
    more than 2-3 examples be generated without good
    reason.
    """
    try:
        assert issubclass(cls, BaseModel), (
            f'{cls.__name__} is not a subclass of '
            f'BaseModel ({getattr(cls, "__mro__")})'
        )
        fields = cls.model_fields
        assert fields, (
            'Could not retrieve fields from the '
            f'{cls.__name__} class; does it have fields, '
            'and do any child models associated with it '
            'have fields?'
        )
        examples = {
            field_name: getattr(field, 'examples', [])
            for field_name, field in fields.items()
        }
        iterables = {
            field_name: [
                (field_name, example_value)
                for example_value in example_values
                if example_value
            ]
            for field_name, example_values
            in examples.items()
            if example_values
        }
        arguments = itertools.product(*iterables.values())
        if max_items is not None and not randomize:
            results = []
            for arg_set in arguments:
                if len(results) == max_items:
                    break
                item_args = dict(arg_set)
                new_item = cls(**item_args).model_dump(mode='json')
                results.append(new_item)
        else:
            results = [
                cls(**dict(arg_set)).model_dump(mode='json')
                for arg_set in arguments
            ]
            if randomize:
                shuffle(results)
            if max_items:
                results = results[0:max_items]
    except (PydanticUserError, AssertionError) as error:
        raise TypeError(f'{error}') from error
    if not isinstance(results, list):
        results = [results]
    return results

# Module Metaclasses

# Module Abstract Base Classes


# Module Concrete Classes
class Address(BaseModel):
    """
    Represents a physical mailing address.
    """  # noqa E501
    street_address: str = Field(
        title='Street Address',
        description='The required street address part of '
        'the address.',
        examples=[
            '1234 Main Street',
        ]
    )
    building_address: Optional[str] | None = Field(
        title='Building Address',
        description='The optional building address part of '
        'the address (the location within a building at '
        'the street_address location).',
        default=None,
        examples=[
            'Suite 123',
            None,
        ]
    )
    city: str = Field(
        title='City',
        description='The required city part of '
        'the address.',
        examples=[
            'Springfield',
            'Franklin',
        ]
    )
    region_name: Optional[str] | None = Field(
        title='Region Name',
        description='The optional region name portion of '
        'the address; typically a state, province, or '
        'some other geographic entity.',
        default=None,
        examples=[
            'New York',
            'Alberta',
            None
        ]
    )
    postal_code: str = Field(
        title='Postal Code',
        description='The required postal code part of '
        'the address; a ZIP Code in the US, or the '
        'equivalent in other countries.',
        examples=[
            '12345',
            '12345-6789',
            'WC1B 4JB',
            'V8X 3X4',
        ]
    )
    country: Optional[str] | None = Field(
        title='Country',
        description='The optional country name portion '
        'of the address. Typically left blank if the '
        'address is in the same country as the sender.',
        default=None,
        examples=[
            'United States',
            'Canada',
            'Great Britain',
            None
        ]
    )


class ProductImage(BaseModel, BaseDataObject):
    """
    Represents an image for a Product in the context of the HMS systems, with data access functionality and operability.
    """  # noqa E501

    CRITERIA_FIELDS: ClassVar[list[str]] = \
        BaseDataObject.CRITERIA_FIELDS + [
            'product_oid', 'is_primary_image'
        ]

    # Relational links
    product_oid: UUID = Field(
        title='Product ID',
        description='The unique identifier of the '
        'Product that the ProductImage is associated '
        'with',
        examples=[
            UUID('0'*32),
            '073f2f01-64b6-441f-a053-b3aaa3cf5a1e',
            UUID('f'*32),
        ],
        frozen=True,
    )

    # Image data
    is_primary_image: bool = Field(
        title='Primary Image Flag',
        description='Flag indicating that this image is '
        'the "primary" image for the product it relates '
        'to, to be used in product lists, and as the '
        '"main" image for product detail views.',
        default=False,
        examples=[
            True,
            False,
        ]
    )
    image_url: HttpUrl = Field(
        title='Image URL',
        description='The required URL of the image',
        examples=[
            'https://cdn.hms.com/products/images/file.png',
        ]
    )
    caption: Optional[str] | None = Field(
        title='Image Caption',
        description='The optional caption for the image.',
        examples=[
            'Some caption text, with <strong>limited'
            '</strong> HTML allowed (styling only).',
            None,
        ]
    )
    alt_text: str = Field(
        title='Image Alt Text',
        description='The required alt-text for the image.',
        examples=[
            'A description of the image for users with '
            'visual impairments. Plain text only.',
        ]
    )
    width: int = Field(
        title='Image Width (pixels)',
        description='The width of the image, in pixels, '
        'as originally uploaded',
        examples=[
            1800,
            1200
        ]
    )
    height: int = Field(
        title='Image Height (pixels)',
        description='The height of the image, in pixels, '
        'as originally uploaded',
        examples=[
            1200,
            1800
        ]
    )


class Product(BaseModel, BaseDataObject):
    """
    Represents a Product in the context of the HMS systems, with data access functionality and operability.
    """  # noqa E501

    CRITERIA_FIELDS: ClassVar[list[str]] = \
        BaseDataObject.CRITERIA_FIELDS + ['artisan_oid']

    # Relational links
    artisan_oid: UUID = Field(
        title='Artisan ID',
        description='The unique identifier of the '
        'Artisan that the Product is associated with',
        examples=[
            UUID('0'*32),
            '073f2f01-64b6-441f-a053-b3aaa3cf5a1e',
            UUID('f'*32),
        ],
        frozen=True,
    )

    # Object data
    name: str = Field(
        title='Product Name',
        description='The required name of the Product.',
        examples=[
            'Billiard Table',
            'Dining Table',
            'Heirloom Quilt',
            'Dragon Scarf',
        ]
    )
    summary: str = Field(
        title='Product Summary',
        description='The required summary of the Product.',
        examples=[
            'Some summary text, with <strong>limited'
            '</strong> HTML allowed (styling only).',
        ]
    )
    description: str = Field(
        title='Product Description',
        description='The required description of the Product.',
        examples=[
            'Some description text, with <strong>limited'
            '</strong> HTML allowed:\n<ul><li>Limited '
            'headings (<code>&lt;h3&gt;</code> and '
            '"higher");</li><li>Limited block-level '
            'elements (paragraphs, lists);</li>'
            '<li>Styling</li></ul>',
        ]
    )
    product_images: Optional[list[ProductImage]] = Field(
        title='Product Images',
        description='The list of ProductImages '
        'associated with the Product',
        default_factory=list,
        examples=[
            [],
            get_examples(ProductImage, max_items=2)
        ]
    )
    # Commerce data
    price: Decimal = Field(
        title='Product Price',
        description='The required price of the Product, '
        'in dollars',
        ge=Decimal(0),
        examples=[
            Decimal(12.34),
            Decimal(123.45),
            Decimal(0),
        ]
    )
    shipping_weight: Decimal = Field(
        title='Shipping Weight',
        description='The required shipping weight of the '
        'Product, in ounces',
        ge=Decimal(0),
        examples=[
            Decimal(320),
            Decimal(3.2),
            Decimal(0),
        ]
    )
    # Size data
    height: Optional[Decimal] | None = Field(
        title='Product Height',
        description='The optional height of the '
        'Product, in inches',
        ge=Decimal(0),
        default=None,
        examples=[
            None,
            Decimal(12),
            Decimal(1),
            Decimal(0),
        ]
    )
    length: Optional[Decimal] | None = Field(
        title='Product Length',
        description='The optional length of the '
        'Product, in inches',
        ge=Decimal(0),
        default=None,
        examples=[
            None,
            Decimal(12),
            Decimal(1),
            Decimal(0),
        ]
    )
    width: Optional[Decimal] | None = Field(
        title='Product Width',
        description='The optional width of the '
        'Product, in inches',
        ge=Decimal(0),
        default=None,
        examples=[
            None,
            Decimal(12),
            Decimal(1),
            Decimal(0),
        ]
    )
    size: Optional[str] | None = Field(
        title='Product Size',
        description='The optional size-name of the '
        'Product.',
        default=None,
        examples=[
            None,
            'Small',
            'Medium',
            'Large'
        ]
    )

    def save(
        self, *,
        db_source_name: str | None = None,
        **metadata: str
    ) -> None:
        """
        Saves the instance's state data to the back end
        data store. OVERRIDES BaseDataObject.save to
        provide the option to save metadata for the
        Product at the same time.

        Parameters:
        -----------
        db_source_name : Optional str
            The name of an alternative table to execute
            the query against during the save.
        metadata : Optional str values
            The metadata values associated with the
            instance to save.

        Note:
        -----
        If no metadata is supplied, existing metadata
        for the Product will be left untouched.
        """
        BaseDataObject.save(self, db_source_name)
        if metadata:
            self.save_metadata(**metadata)

    def save_metadata(self, **metadata: str) -> None:
        """
        Creates metadata records for the instance,
        deleting and overwriting any existing ones
        in the process.
        """
        connector = get_env_database_connector()
        cursor = connector.cursor()
        cursor.execute(
            "DELETE FROM ProductMetadata "
            "WHERE product_oid='%s';",
            (self.oid)
        )
        for key, value in metadata.items():
            cursor.execute(
                "INSERT INTO ProductMetadata "
                "(product_oid, category_name, value) "
                "VALUES ('%s', '%s', '%s')",
                (self.oid, key, value)
            )
        connector.commit()


class Artisan(BaseModel, BaseDataObject):
    """
    Represents an Artisan in the context of the HMS systems, with data access functionality and operability.
    """  # noqa E501

    # Person-name information fields
    honorific: Optional[str] | None = Field(
        title='Honorific',
        description='The optional honorific for the '
        'Artisan.',
        default=None,
        examples=[
            # Gender-indicative
            'Mr.', 'Mrs.', 'Miss', 'Ms.',
            # Gender-neutral
            'Mx.',
            # Profession-indicative
            'Dr.', 'Rev.',
            # If not supplied
            None,
        ]
    )
    given_name: str = Field(
        title='First/Given Name',
        description='The required given name ("first '
        'name" in western traditions) of the Artisan.',
        examples=[
            # Western tradition
            'John', 'Jane',
            # Chinese tradition
            'Jun', 'Jing'
        ]
    )
    middle_name: Optional[str] | None = Field(
        title='Middle Name',
        description='The optional middle name or '
        'initial(s) of the Artisan.',
        default=None,
        examples=[
            'Robert', 'Erin',
            # If not supplied
            None,
        ]
    )
    family_name: str = Field(
        title='Last/Family Name',
        description='The required family name ("last '
        'name" in western traditions) of the Artisan.',
        examples=[
            # Western tradition
            'Jones', 'Smith',
            # Chinese tradition
            'Chen', 'Huang'
        ]
    )
    suffix: Optional[str] | None = Field(
        title='Suffix',
        description='The optional suffix for the '
        "Artisan's name.",
        default=None,
        examples=[
            # American tradition
            'Jr.', 'Sr.', 'III',
            # British tradition
            'Jnr.', 'Snr.',
            # If not supplied
            None,
        ]
    )
    # Company information
    company_name: Optional[str] | None = Field(
        title='Company Name',
        description='The optional company name for '
        'the Artisan.',
        default=None,
        examples=[
            'Jones Woodworking', 'Smith Fiber Crafts',
            # If not supplied
            None,
        ]
    )
    # Contact information
    business_address: Address = Field(
        title='Business Mailing Address',
        description='The required mailing address for '
        'the Artisan.',
        examples=get_examples(Address, max_items=2)
    )
    email_address: EmailStr | NameEmail = Field(
        title='Email Address',
        description='The required email address for the '
        'Artisan. May be either a simple email, or a '
        '"name" email (see examples).',
        examples=[
            'John Smith <john.smith@test.com>',
            'Company Contact <contact@company.com>',
            'john.smith@test.com',
            'contact@company.com',
        ]
    )
    # Artisan Products collection
    products: Optional[list[Product]] = Field(
        title='Products',
        description='The list of Products associated '
        'with the Artisan',
        default_factory=list,
        examples=[
            [],
            get_examples(Product, max_items=2)
        ]
    )


# Code to run if the module is executed directly
if __name__ == '__main__':

    pass
