#!/usr/bin/env python3.11
"""
Provides the backing Lambda Function for the API endpoint
that handles delete product functionality.
"""
from __future__ import annotations

# Built-In Imports
import json
import os

from pathlib import Path

# Third-Party Imports
from hms.core.business_objects import \
    Product, ProductNotFoundError, \
    ProductImage, ProductImageNotFoundError

from awslambdaric.lambda_context import LambdaContext
from goblinfish.metrics.trackers import ProcessTracker

# Path Manipulations (avoid these!) and "Local" Imports
from logger import logger

# Module "Constants" and Other Attributes
tracker = ProcessTracker()

module = Path(__file__).stem

LambdaProxyInput = dict[str, str]
LambdaProxyOutput = dict[str, str]

# Lambda Handlers

@tracker
def api_handler(
    event: LambdaProxyInput, context: LambdaContext
) -> LambdaProxyOutput:
    """
    The delete handler for product targets
    in the artisan scope.

    Parameters:
    -----------
    event : LambdaProxyInput (dict)
        The API event to be handled.
    context : LambdaContext
        The standard Lambda context object provided
        by AWS during a Lambda invocation.
    """
    try:

        _authnz_preflight()

        # Get the oid of the Artisan deleting the
        # product, and of the Product to be deleted
        artisan_oid = event.get(
            'pathParameters', {}
        ).get('artisan_oid')
        if artisan_oid is None \
                or len(artisan_oid.split(',')) != 1:
            raise ValueError(
                f'{module}.api_handler requires a '
                'single artisan_oid, but that path '
                f'parameter resolved to "{artisan_oid}" '
                f'({type(artisan_oid).__name__}).'
            )
        product_oid = event.get(
            'pathParameters', {}
        ).get('oid')
        if product_oid is None \
                or len(product_oid.split(',')) != 1:
            raise ValueError(
                f'{module}.api_handler requires a single '
                'oid, but that path parameter resolved to '
                f'"{product_oid}" ({type(product_oid).__name__}).'
            )

        # Get the Product objects, keeping track of how
        # long the process takes for metrics purposes
        with tracker.timer('product_db_access'):
            products = Product.get(
                product_oid,
                db_source_name='Products',
                artisan_oid=artisan_oid
            )
        # Raise an error if no Product could be found
        if len(products) == 0:
            raise ProductNotFoundError(
                'Could not retrieve a Product '
                f'identified by "{product_oid}".'
            )
        product = products[0]
        logger.debug('product: {product}')

        with tracker.timer('product_image_db_access'):
            product.product_images = ProductImage.get(
                db_source_name='ProductImages',
                product_oid=product_oid
            )
        image_oids = [
            img.oid for img in product.product_images
        ]

        _authnz_reconcile()

        # Perform the actual deletion(s)
        for image_oid in image_oids:
            for location in (
                os.environ['ORIGINAL_IMAGES_LOCATION'],
                os.environ['DETAIL_IMAGES_LOCATION'],
                os.environ['THUMBNAIL_IMAGES_LOCATION'],
            ):
                delete_image(location, image_oid)
        ProductImage.delete(
            *image_oids,
            db_source_name='ProductImages',
        )
        Product.delete(
            product_oid,
            db_source_name='Products',
        )

        result = {
            'statusCode': 200,
            'body': product.model_dump_json()
        }


    except (
        ProductNotFoundError, ProductImageNotFoundError
    ) as error:
        logger.exception(
            f'{error.__class__.__name__}: {error} '
            'occured in api_handler'
        )
        logger.error(f'event: {json.dumps(event)}')
        logger.error(f'context: {repr(context)}')
        result = {
            'statusCode': 404,
            'body': 'Not Found: '
            f'({context.aws_request_id})'
        }

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
def _authnz_preflight(*args, **kwargs):
    ...


def _authnz_reconcile(*args, **kwargs):
    ...


def delete_image(location: str, oid: str) -> None:
    """
    Deletes the image from the specified location.

    Parameters:
    -----------
    location : str (local file path or S3 URL)
        The location to write the image data to
    oid : str (UUID format)
        The oid of the image, used to create a common
        file name for the original, detail and thumbnail
        images that is distinct from any other image's
        original, detail and thumbnail file names.

    Raises:
    -------
    NotImplementedError
        If called with an S3 URL as the location.
        This will be implemented later.

    Notes:
    ------
    * If the location is a local file URL (starting with
      "file:///"), the file will be written to the local
      file system at that location.
    * If the location is an S3 URL, then the file will be
      written to the S3 bucket and path specified.
    """
    logger.info(f'{module}.save_image called')
    logger.debug(f'vars: {vars()}')

    image_name = f'{oid}.png'

    if location.startswith('s3://'):
        raise NotImplementedError(
            'Deleting images from an S3 bucket is not '
            'yet supported.'
        )
    elif location.startswith('file:///'):
        save_path = Path(
            location[8:].format(**os.environ)
        )
        logger.debug(
            f'save_path: {save_path} '
            f'({type(save_path).__name__})'
        )
        image_path = save_path / image_name
        if image_path.exists():
            image_path.unlink()
        logger.info(
            f'{module}.delete_image completed: '
            f'deleted {image_path}'
        )

    else:
        raise RuntimeError(
            f'Unsupported location type ({location}) '
            'to save image files.'
        )
    logger.info(f'{module}.save_image completed')


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
