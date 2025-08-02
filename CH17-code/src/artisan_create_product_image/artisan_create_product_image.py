#!/usr/bin/env python3.11
"""
Provides the backing Lambda Function for the API endpoint
that handles create product_image functionality.
"""
from __future__ import annotations

# Built-In Imports
import io
import json
import os

from base64 import b64decode
from collections import namedtuple
from pathlib import Path
from uuid import uuid4

# Third-Party Imports
from PIL import Image
from awslambdaric.lambda_context import LambdaContext
from goblinfish.metrics.trackers import ProcessTracker

# Path Manipulations (avoid these!) and "Local" Imports
from hms.core.business_objects import ProductImage, \
    Product, ProductNotFoundError

from logger import logger

# Custom Exceptions
class VirusScanFailedError(Exception):
    """
    An error to be raised if an external virus-scanning
    API detected a virus.
    """
    ...

# Module "Constants" and Other Attributes
tracker = ProcessTracker()

module = Path(__file__).stem

LambdaProxyInput = dict[str, str]
LambdaProxyOutput = dict[str, str]

ALLOWED_MIME_TYPES = {
    'JPEG': 'image/jpeg',
    'PNG': 'image/png'
}
FORMAT_TO_FILE_EXT = {
    'JPEG': 'jpg',
    'PNG': 'png'
}

ImageAndSize = namedtuple(
    'ImageAndSize',
    ['image', 'width', 'height']
)

# Lambda Handlers

@tracker
def api_handler(
    event: LambdaProxyInput, context: LambdaContext
) -> LambdaProxyOutput:
    """
    The create handler for product_image targets
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
        logger.info(f'{module}.api_handler called')
        logger.debug(f'event: {json.dumps(event)}')
        logger.debug(f'context: {repr(context)}')

        _authnz_preflight()

        # Get the event body and make sure it's
        # what's expected
        body = json.loads(event.get('body', 'null'))
        assert body is not None, (
            'No "body" present in event'
        )

        # Get the oid of the Product to be updated
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
                product_oid, db_source_name='Products'
            )
        # Raise an error if no Product could be found
        if len(products) == 0:
            raise ProductNotFoundError(
                'Could not retrieve a Product '
                f'identified by "{product_oid}".'
            )

        # Get and check the image data
        image_base64_str = body['image_data'] \
            .split(',')[-1].strip()
        assert image_base64_str, (
            'No "image_data" present in event.body'
        )

        # Use the string representation for virus
        # checking with external API calls
        _call_virus_check_api(image_base64_str)

        # Decode the Base 64 string to get the
        # actual binary data for the file
        image_base64 = bytes(image_base64_str, 'utf-8')
        original_image = b64decode(image_base64)
        image_io = io.BytesIO(original_image)
        image = Image.open(image_io)
        logger.debug(
            f'image: format={image.format} '
            f'({Image.MIME.get(image.format)}) '
            f'width={image.width} height={image.height}'
        )
        assert Image.MIME.get(image.format) \
            in ALLOWED_MIME_TYPES.values(), (
            'Uploads must be one of '
            f'{list(ALLOWED_MIME_TYPES.keys())} '
            'file types.'
        )

        # Resize and convert the image as needed to
        # create a product-detail image
        detail_image = _create_detail_image(image)

        # Resize and convert the image as needed to
        # create a product-thumbnail image
        thumbnail_image = _create_thumbnail_image(image)

        # Save the image files to the appropriate
        # locations
        # Use a common oid for each
        new_image_oid = body.get('oid', str(uuid4()))
        # Save the original image
        save_image(
            image,
            os.environ['ORIGINAL_IMAGES_LOCATION'],
            new_image_oid
        )
        # The detail image
        save_image(
            detail_image,
            os.environ['DETAIL_IMAGES_LOCATION'],
            new_image_oid
        )
        # The thumbnail image
        save_image(
            thumbnail_image,
            os.environ['THUMBNAIL_IMAGES_LOCATION'],
            new_image_oid
        )

        request_params = {
            'oid': new_image_oid,
            'product_oid': product_oid,
            'caption':body.get('caption'),
            'alt_text':body['alt_text'],
        }

        image_params = {
            'original_image_size': {
                'width': image.width,
                'height': image.height,
            },
            'detail_image_size': {
                'width': detail_image.width,
                'height': detail_image.height,
            },
            'thumbnail_image_size': {
                'width': thumbnail_image.width,
                'height': thumbnail_image.height,
            },
        }

        new_product_image = ProductImage(
            **image_params | request_params
        )

        result = {
            'statusCode': 200,
            'body': new_product_image.model_dump_json()
        }

        _authnz_reconcile()


    except (AssertionError, TypeError, ValueError) as error:
        logger.exception(
            f'{error.__class__.__name__}: {error} '
            'occured in api_handler'
        )
        logger.error(f'event: {json.dumps(event)}')
        logger.error(f'context: {repr(context)}')
        result = {
            'statusCode': 400,
            'body': 'Bad Request: '
            f'({context.aws_request_id})'
        }

    except VirusScanFailedError as error:
        logger.exception(
            f'{error.__class__.__name__}: {error} '
            'occured in api_handler'
        )
        logger.error(f'event: {json.dumps(event)}')
        logger.error(f'context: {repr(context)}')
        result = {
            'statusCode': 422,
            'body': 'Unprocessable Content: '
            f'({context.aws_request_id}). '
            'The submitted file did not pass a virus check'
        }

    except ProductNotFoundError as error:
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


def _call_virus_check_api(image_base64_str: str):
    """
    Submits the supplied base64-encoded string to an
    external virus-checking API. If the results of
    the check indicate a virus, raises a
    VirusScanFailedError
    """
    # TODO: Implement the actual API call.
    ...


def _create_detail_image(original_image: Image) -> Image:
    """
    Placeholder code
    """
    # TODO: Handle the maximum size, scaling, cropping,
    #       etc. based on business rules for detail
    #       images that are TBD.
    # For now, just return the original image and its
    # width and height.
    return original_image


def _create_thumbnail_image(original_image: bytes) -> Image:
    """
    Placeholder code
    """
    # TODO: Handle the maximum size, scaling, cropping,
    #       etc. based on business rules for detail
    #       images that are TBD.
    # For now, just return the original image and its
    # width and height.
    return original_image


def save_image(image: Image, location: str, oid: str) -> None:
    """
    Saves the image to the specified location.

    Parameters:
    -----------
    image : Image
        The pillow Image data to write.
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
            'Saving images to an S3 bucket is not yet '
            'supported.'
        )
    elif location.startswith('file:///'):
        save_path = Path(
            location[8:].format(**os.environ)
        )
        logger.debug(
            f'save_path: {save_path} '
            f'({type(save_path).__name__})'
        )
        if not save_path.exists():
            logger.debug(f'Creating {save_path} directory')
            save_path.mkdir(parents=True)
        image_path = save_path / image_name
        image.save(image_path)
        logger.info(
            f'{module}.save_image completed: {image} '
            f'saved to {image_path}'
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
