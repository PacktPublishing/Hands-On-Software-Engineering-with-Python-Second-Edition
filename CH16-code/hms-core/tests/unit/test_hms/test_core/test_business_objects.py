#!/usr/bin/env python3.11
"""
"""

# Built-In Imports
import unittest

from datetime import datetime
from uuid import UUID

# Third-Party Imports
from pydantic import ValidationError

# Path Manipulations (avoid these!) and "Local" Imports
from hms.core.data_objects import \
    BaseDataObject, get_examples

# Import the test target
from hms.core.business_objects import \
    Address, Artisan, Product, ProductImage


# Expected test-case classes
class test_Address(unittest.TestCase):
    """
    Tests the Address class.
    """
    EXAMPLE_ARGS = get_examples(
        Address, max_items=1
    )[0]

    def test_street_address(self):
        """
        Tests the street_address field of the
        Address class
        """
        # Arrange
        good_values = Address. \
            model_fields['street_address'].examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'street_address'
        }
        for street_address in good_values:
            with self.subTest(
                msg=f'Testing creation with street_'
                f'address {street_address} '
                f'({type(street_address).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['street_address'] = \
                    street_address
                # Act
                inst = Address(**args)
                # Assert
                self.assertEqual(
                    inst.street_address, expected,
                    'Creating an Address with a street_'
                    f'address value of "{street_address}"'
                    f' ({type(street_address).__name__}) '
                    'should return that value in instance'
                    f'.street_address, but '
                    f'"{inst.street_address}" '
                    f'({type(street_address).__name__}) '
                    'was returned instead.'
                )

    def test_building_address(self):
        """
        Tests the building_address field of the
        Address class
        """
        # Arrange
        good_values = Address. \
            model_fields['building_address'].examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'building_address'
        }
        for building_address in good_values:
            with self.subTest(
                msg=f'Testing creation with building_address '
                f'{building_address} ({type(building_address).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['building_address'] = \
                    building_address
                # Act
                inst = Address(**args)
                # Assert
                self.assertEqual(
                    inst.building_address, expected,
                    'Creating an Address with a building_'
                    f'address value of "{building_address}" '
                    f'({type(building_address).__name__}) '
                    'should return that value in instance'
                    f'.building_address, but "{inst.building_address}" '
                    f'({type(building_address).__name__}) was '
                    'returned instead.'
                )

    def test_city(self):
        """
        Tests the city field of the Address class
        """
        # Arrange
        good_values = Address.model_fields['city'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'city'
        }
        for city in good_values:
            with self.subTest(
                msg=f'Testing creation with city '
                f'{city} ({type(city).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['city'] = city
                # Act
                inst = Address(**args)
                # Assert
                self.assertEqual(
                    inst.city, expected,
                    'Creating an Address with '
                    f'a city value of "{city}" '
                    f'({type(city).__name__}) '
                    'should return that value in instance'
                    f'.city, but "{inst.city}" '
                    f'({type(city).__name__}) was '
                    'returned instead.'
                )

    def test_region_name(self):
        """
        Tests the region_name field of the Address class
        """
        # Arrange
        good_values = Address. \
            model_fields['region_name'].examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'region_name'
        }
        for region_name in good_values:
            with self.subTest(
                msg=f'Testing creation with region_name '
                f'{region_name} ({type(region_name).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['region_name'] = \
                    region_name
                # Act
                inst = Address(**args)
                # Assert
                self.assertEqual(
                    inst.region_name, expected,
                    'Creating an Address with '
                    f'a region_name value of "{region_name}" '
                    f'({type(region_name).__name__}) '
                    'should return that value in instance'
                    f'.region_name, but "{inst.region_name}" '
                    f'({type(region_name).__name__}) was '
                    'returned instead.'
                )

    def test_postal_code(self):
        """
        Tests the postal_code field of the Address class
        """
        # Arrange
        good_values = Address. \
            model_fields['postal_code'].examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'postal_code'
        }
        for postal_code in good_values:
            with self.subTest(
                msg=f'Testing creation with postal_code '
                f'{postal_code} ({type(postal_code).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['postal_code'] = \
                    postal_code
                # Act
                inst = Address(**args)
                # Assert
                self.assertEqual(
                    inst.postal_code, expected,
                    'Creating an Address with '
                    f'a postal_code value of "{postal_code}" '
                    f'({type(postal_code).__name__}) '
                    'should return that value in instance'
                    f'.postal_code, but "{inst.postal_code}" '
                    f'({type(postal_code).__name__}) was '
                    'returned instead.'
                )

    def test_country(self):
        """
        Tests the country field of the BaseDataObject class
        """
        # Arrange
        good_values = Address. \
            model_fields['country'].examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'country'
        }
        for country in good_values:
            with self.subTest(
                msg=f'Testing creation with country '
                f'{country} ({type(country).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['country'] = country
                # Act
                inst = Address(**args)
                # Assert
                self.assertEqual(
                    inst.country, expected,
                    'Creating an Address with '
                    f'a country value of "{country}" '
                    f'({type(country).__name__}) '
                    'should return that value in instance'
                    f'.country, but "{inst.country}" '
                    f'({type(country).__name__}) was '
                    'returned instead.'
                )


class test_Artisan(unittest.TestCase):
    """
    Tests the Artisan class.
    """

    EXAMPLE_ARGS = get_examples(
        Artisan, max_items=1
    )[0]

    # Tests of the inherited fields
    @unittest.skipIf(
        Artisan.oid is BaseDataObject.oid,
        'The oid field is inherited from BaseDataObject'
    )
    def test_oid(self):
        self.fail(
            'Artisan.oid was originally inherited from '
            'BaseDataObject, but that has changed, and '
            'it needs to be tested in relation to the '
            'Artisan class'
        )

    @unittest.skipIf(
        Artisan.is_active is BaseDataObject.is_active,
        'The is_active field is inherited from BaseDataObject'
    )
    def test_is_active(self):
        self.fail(
            'Artisan.is_active was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the Artisan class'
        )

    @unittest.skipIf(
        Artisan.is_deleted is BaseDataObject.is_deleted,
        'The is_deleted field is inherited from BaseDataObject'
    )
    def test_is_deleted(self):
        self.fail(
            'Artisan.is_deleted was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the Artisan class'
        )

    @unittest.skipIf(
        Artisan.created is BaseDataObject.created,
        'The created field is inherited from '
        'BaseDataObject'
    )
    def test_created(self):
        self.fail(
            'Artisan.created was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the Artisan class'
        )

    @unittest.skipIf(
        Artisan.modified is BaseDataObject.modified,
        'The modified field is inherited from '
        'BaseDataObject'
    )
    def test_modified(self):
        self.fail(
            'Artisan.modified was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the Artisan class'
        )

    def test_honorific(self):
        """
        Tests the honorific field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['honorific'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'honorific'
        }
        for honorific in good_values:
            with self.subTest(
                msg=f'Testing creation with honorific '
                f'{honorific} ({type(honorific).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['honorific'] = honorific
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.honorific, expected,
                    'Creating an Artisan with '
                    f'a honorific value of "{honorific}" '
                    f'({type(honorific).__name__}) '
                    'should return that value in instance'
                    f'.honorific, but "{inst.honorific}" '
                    f'({type(honorific).__name__}) was '
                    'returned instead.'
                )

    def test_given_name(self):
        """
        Tests the given_name field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['given_name'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'given_name'
        }
        for given_name in good_values:
            with self.subTest(
                msg=f'Testing creation with given_name '
                f'{given_name} ({type(given_name).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['given_name'] = given_name
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.given_name, expected,
                    'Creating an Artisan with '
                    f'a given_name value of "{given_name}" '
                    f'({type(given_name).__name__}) '
                    'should return that value in instance'
                    f'.given_name, but "{inst.given_name}" '
                    f'({type(given_name).__name__}) was '
                    'returned instead.'
                )

    def test_middle_name(self):
        """
        Tests the middle_name field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['middle_name'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'middle_name'
        }
        for middle_name in good_values:
            with self.subTest(
                msg=f'Testing creation with middle_name '
                f'{middle_name} ({type(middle_name).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['middle_name'] = middle_name
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.middle_name, expected,
                    'Creating an Artisan with '
                    f'a middle_name value of "{middle_name}" '
                    f'({type(middle_name).__name__}) '
                    'should return that value in instance'
                    f'.middle_name, but "{inst.middle_name}" '
                    f'({type(middle_name).__name__}) was '
                    'returned instead.'
                )

    def test_family_name(self):
        """
        Tests the family_name field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['family_name'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'family_name'
        }
        for family_name in good_values:
            with self.subTest(
                msg=f'Testing creation with family_name '
                f'{family_name} ({type(family_name).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['family_name'] = family_name
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.family_name, expected,
                    'Creating an Artisan with '
                    f'a family_name value of "{family_name}" '
                    f'({type(family_name).__name__}) '
                    'should return that value in instance'
                    f'.family_name, but "{inst.family_name}" '
                    f'({type(family_name).__name__}) was '
                    'returned instead.'
                )

    def test_suffix(self):
        """
        Tests the suffix field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['suffix'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'suffix'
        }
        for suffix in good_values:
            with self.subTest(
                msg=f'Testing creation with suffix '
                f'{suffix} ({type(suffix).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['suffix'] = suffix
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.suffix, expected,
                    'Creating an Artisan with '
                    f'a suffix value of "{suffix}" '
                    f'({type(suffix).__name__}) '
                    'should return that value in instance'
                    f'.suffix, but "{inst.suffix}" '
                    f'({type(suffix).__name__}) was '
                    'returned instead.'
                )

    def test_company_name(self):
        """
        Tests the company_name field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['company_name'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'company_name'
        }
        for company_name in good_values:
            with self.subTest(
                msg=f'Testing creation with company_name '
                f'{company_name} ({type(company_name).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['company_name'] = company_name
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.company_name, expected,
                    'Creating an Artisan with '
                    f'a company_name value of "{company_name}" '
                    f'({type(company_name).__name__}) '
                    'should return that value in instance'
                    f'.company_name, but "{inst.company_name}" '
                    f'({type(company_name).__name__}) was '
                    'returned instead.'
                )

    @unittest.skip('Needs more detailed attention')
    def test_business_address(self):
        """
        Tests the business_address field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['business_address'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'business_address'
        }
        for business_address in good_values:
            with self.subTest(
                msg=f'Testing creation with business_address '
                f'{business_address} ({type(business_address).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['business_address'] = business_address
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.business_address, expected,
                    'Creating an Artisan with '
                    f'a business_address value of "{business_address}" '
                    f'({type(business_address).__name__}) '
                    'should return that value in instance'
                    f'.business_address, but "{inst.business_address}" '
                    f'({type(business_address).__name__}) was '
                    'returned instead.'
                )

    def test_email_address(self):
        """
        Tests the email_address field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['email_address'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'email_address'
        }
        for email_address in good_values:
            with self.subTest(
                msg=f'Testing creation with email_address '
                f'{email_address} ({type(email_address).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['email_address'] = email_address
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.email_address, expected,
                    'Creating an Artisan with '
                    f'a email_address value of "{email_address}" '
                    f'({type(email_address).__name__}) '
                    'should return that value in instance'
                    f'.email_address, but "{inst.email_address}" '
                    f'({type(email_address).__name__}) was '
                    'returned instead.'
                )

    @unittest.skip('Needs more detailed attention')
    def test_products(self):
        """
        Tests the products field of the Artisan class
        """
        # Arrange
        good_values = Artisan.model_fields['products'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'products'
        }
        for products in good_values:
            with self.subTest(
                msg=f'Testing creation with products '
                f'{products} ({type(products).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                expected = args['products'] = products
                # Act
                inst = Artisan(**args)
                # Assert
                self.assertEqual(
                    inst.products, expected,
                    'Creating an Artisan with '
                    f'a products value of "{products}" '
                    f'({type(products).__name__}) '
                    'should return that value in instance'
                    f'.products, but "{inst.products}" '
                    f'({type(products).__name__}) was '
                    'returned instead.'
                )


class test_Product(unittest.TestCase):
    """
    Tests the Product class.
    """

    EXAMPLE_ARGS = get_examples(
        Product, max_items=1
    )[0]

    # Tests of the inherited fields
    @unittest.skipIf(
        Product.oid is BaseDataObject.oid,
        'The oid field is inherited from BaseDataObject'
    )
    def test_oid(self):
        self.fail(
            'Product.oid was originally inherited from '
            'BaseDataObject, but that has changed, and '
            'it needs to be tested in relation to the '
            'Product class'
        )

    @unittest.skipIf(
        Product.is_active is BaseDataObject.is_active,
        'The is_active field is inherited from '
        'BaseDataObject'
    )
    def test_is_active(self):
        self.fail(
            'Product.is_active was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the Product class'
        )

    @unittest.skipIf(
        Product.is_deleted is BaseDataObject.is_deleted,
        'The is_deleted field is inherited from '
        'BaseDataObject'
    )
    def test_is_deleted(self):
        self.fail(
            'Product.is_deleted was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the Product class'
        )

    @unittest.skipIf(
        Product.created is BaseDataObject.created,
        'The created field is inherited from '
        'BaseDataObject'
    )
    def test_created(self):
        self.fail(
            'Product.created was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the Product class'
        )

    @unittest.skipIf(
        Product.modified is BaseDataObject.modified,
        'The modified field is inherited from '
        'BaseDataObject'
    )
    def test_modified(self):
        self.fail(
            'Product.modified was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the Product class'
        )

    def test_artisan_oid(self):
        """
        Tests the artisan_oid field of the Product class
        """
        # Arrange
        good_values = Product.model_fields['artisan_oid'] \
            .examples
        base_args = {
            key: value for key, value
            in self.EXAMPLE_ARGS.items()
            if key != 'artisan_oid'
        }
        for artisan_oid in good_values:
            with self.subTest(
                msg=f'Testing creation with artisan_oid {artisan_oid} '
                f'({type(artisan_oid).__name__}'
            ):
                # Arrange
                args = dict(base_args)
                args['artisan_oid'] = artisan_oid
                if isinstance(artisan_oid, str):
                    expected = UUID(artisan_oid)
                else:
                    expected = artisan_oid
                # Act
                inst = Product(**args)
                # Assert
                self.assertEqual(
                    inst.artisan_oid, expected,
                    'Creating a ConcreteDataObject '
                    f'with an artisan_oid value of "{artisan_oid}" '
                    f'({type(artisan_oid).__name__}) should '
                    'return that value in instance.artisan_oid, '
                    f'but "{inst.artisan_oid}" '
                    f'({type(artisan_oid).__name__}) was '
                    'returned instead.'
                )
        with self.subTest(
            msg='Testing that an artisan_oid cannot be changed '
            'after it is set'
        ):
            with self.assertRaises(ValidationError):
                inst.artisan_oid = UUID('0'*32)
        with self.subTest(
            msg='Testing that an artisan_oid cannot be deleted'
        ):
            with self.assertRaises(ValidationError):
                del inst.artisan_oid


class test_ProductImage(unittest.TestCase):
    """
    Tests the ProductImage class.
    """

    EXAMPLE_ARGS = get_examples(
        ProductImage, max_items=1
    )[0]

    # Tests of the inherited fields
    @unittest.skipIf(
        ProductImage.oid is BaseDataObject.oid,
        'The oid field is inherited from BaseDataObject'
    )
    def test_oid(self):
        self.fail(
            'ProductImage.oid was originally inherited '
            'from BaseDataObject, but that has changed, '
            'and it needs to be tested in relation to '
            'the ProductImage class'
        )

    @unittest.skipIf(
        ProductImage.is_active
        is BaseDataObject.is_active,
        'The is_active field is inherited from '
        'BaseDataObject'
    )
    def test_is_active(self):
        self.fail(
            'ProductImage.is_active was originally '
            'inherited from BaseDataObject, but that '
            'has changed, and it needs to be tested in '
            'relation to the ProductImage class'
        )

    @unittest.skipIf(
        ProductImage.is_deleted is
        BaseDataObject.is_deleted,
        'The is_deleted field is inherited from '
        'BaseDataObject'
    )
    def test_is_deleted(self):
        self.fail(
            'ProductImage.is_deleted was originally '
            'inherited from BaseDataObject, but that '
            'has changed, and it needs to be tested in '
            'relation to the ProductImage class'
        )

    @unittest.skipIf(
        ProductImage.created is BaseDataObject.created,
        'The created field is inherited from '
        'BaseDataObject'
    )
    def test_created(self):
        self.fail(
            'ProductImage.created was originally '
            'inherited from BaseDataObject, but that '
            'has changed, and it needs to be tested in '
            'relation to the ProductImage class'
        )

    @unittest.skipIf(
        ProductImage.modified is BaseDataObject.modified,
        'The modified field is inherited from '
        'BaseDataObject'
    )
    def test_modified(self):
        self.fail(
            'ProductImage.modified was originally '
            'inherited from BaseDataObject, but that '
            'has changed, and it needs to be tested in '
            'relation to the ProductImage class'
        )

# Code to run if the module is executed directly
if __name__ == '__main__':

    # ~ unittest.main()

    import pytest
    # ~ pytest.main([__file__, '-v'])
    # ~ pytest.main([f'{__file__}::test_Artisan', '-v'])
    pytest.main([f'{__file__}::test_Product::test_artisan_oid', '-vv'])
