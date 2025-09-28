#!/usr/bin/env python3.11
"""
Provides the backing Lambda Function for the API endpoint
that handles read products functionality.
"""
from __future__ import annotations

# Built-In Imports
import json

from pathlib import Path
from uuid import UUID

# Third-Party Imports
from hms.core.business_objects import Product, \
    ProductImage

from awslambdaric.lambda_context import LambdaContext
from goblinfish.metrics.trackers import ProcessTracker

# Path Manipulations (avoid these!) and "Local" Imports
from logger import logger

# Module "Constants" and Other Attributes
tracker = ProcessTracker()

module = Path(__file__).stem

LambdaProxyInput = dict[str, str]
LambdaProxyOutput = dict[str, str]

PRODUCT_FIELD_NAMES = (
    # Unique identifier
    'oid',
    # Product fields
    'name',
    'summary',
    'product_images',
    'price',
)
PRODUCT_IMAGE_FIELD_NAMES = (
    # Unique identifier
    'oid',
    # ProductImage fields
    'is_primary_image',
    'alt_text',
    'thumbnail_image_size',
)


# Lambda Handlers

@tracker
def api_handler(
    event: LambdaProxyInput, context: LambdaContext
) -> LambdaProxyOutput:
    """
    The read handler for products targets
    in the public scope.

    Parameters:
    -----------
    event : LambdaProxyInput (dict)
        The API event to be handled.
        Fields that contribute to the response include
        queryStringParameters:
        page_size: int
            The number of items to return in a single
            page of results.
        page_number : int
            The page-number of resuls to return
            (zero-indexed)
        sort_{field-name} : str ("asc" or "desc")
            Sorts the {field-name} field in ascending
            ("asc") or descending ("desc") order.
    context : LambdaContext
        The standard Lambda context object provided
        by AWS during a Lambda invocation.
    """
    try:
        logger.info(f'{module}.api_handler called')
        logger.debug(f'event: {json.dumps(event)}')
        logger.debug(f'context: {repr(context)}')

        # Convert the query-strings for pagination
        get_params = event.get('queryStringParameters') or {}
        pagination_params = {
            key: int(get_params.get(key, 0)) or None
            for key in ('page_size', 'page_number')
        }
        get_params.update(pagination_params)
        logger.debug(f'get_params: {get_params}')

        # Get the Product objects, keeping track of how
        # long the process takes for metrics purposes
        with tracker.timer('product_db_access'):
            products = Product.get(
                db_source_name='Products', **get_params,
                is_active=True, is_deleted=False,
            )
        # Get the ProductImage objects, keeping track of
        # how long the process takes for metrics purposes
        product_oids = [str(prod.oid) for prod in products]
        logger.debug(f'product_oids: {product_oids}')
        with tracker.timer('product_image_db_access'):
            product_images = ProductImage.get(
                db_source_name='ProductImages',
                product_oid_in=product_oids,
                is_active=True, is_deleted=False,
            )
            logger.debug(f'product_images: {product_images}')
        with tracker.timer('product_image_selection'):
            product_image_dict = {
                UUID(oid): [] for oid in product_oids
            }
            for product_image in product_images:
                product_image_dict[product_image.product_oid].append(product_image)

        # Filter the results' fields
        results = [
            {
                key: value for key, value
                in product.model_dump(mode='json').items()
                if key in PRODUCT_FIELD_NAMES
            }
            for product in products
        ]
        for item in results:
            product_oid = UUID(item['oid'])
            if product_image_dict[product_oid]:
                image = sorted(
                    product_image_dict[product_oid],
                    key = lambda img: img.is_primary_image,
                    reverse=True
                )[0]
                item['product_images'] = [
                    {
                        key: value for key, value
                        in image.model_dump(mode='json').items()
                        if key in PRODUCT_IMAGE_FIELD_NAMES
                    }
                ]
        body = json.dumps(results)
        result = {
            'statusCode': 200,
            'body': body
        }

    # TODO: Add other exception-handling if needed

    except Exception as error:
        logger.exception(
            f'{error.__class__.__name__}: {error} '
            'occured in api_handler'
        )
        logger.error(f'event: {json.dumps(event)}')
        logger.error(f'context: {repr(context)}')
        result = {
            'statusCode': 500,
            'body': 'Internal Server Error: '
            f'({context.aws_request_id})'
        }

    logger.info(f'{module}.api_handler complete')
    logger.debug(f'result: {json.dumps(result)}')
    return result


# Helper Functions

# Module Metaclasses (if any)

# Module Abstract Base Classes (if any, requires abc)

# Module Concrete Classes

# Code to run if the module is executed directly

if __name__ == '__main__':

    import logging

    from os import sep, extsep

    formatter = logging.Formatter(
        "[%(levelname)s]  %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    module = __file__.split(sep)[-1].split(extsep)[0]
    logger.info(f'Running {module}.__main__')
    result = api_handler({}, None)
    logger.info(
        'api_handler result: '
        f'{json.dumps(result, indent=4)}'
    )
    logger.info(f'{module}.__main__ completed')
