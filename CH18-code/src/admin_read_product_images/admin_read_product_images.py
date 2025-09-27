#!/usr/bin/env python3.11
"""
Provides the backing Lambda Function for the API endpoint
that handles read product_images functionality.
"""
from __future__ import annotations

# Built-In Imports
import json

from pathlib import Path

# Third-Party Imports
from awslambdaric.lambda_context import LambdaContext
from goblinfish.metrics.trackers import ProcessTracker

# Path Manipulations (avoid these!) and "Local" Imports
from hms.core.business_objects import ProductImage

from logger import logger

# Module "Constants" and Other Attributes
tracker = ProcessTracker()

module = Path(__file__).stem

LambdaProxyInput = dict[str, str]
LambdaProxyOutput = dict[str, str]

LIST_FIELD_NAMES = (
    # Unique identifier
    'oid',
    # Status fields
    'is_active', 'is_deleted',
    # Date/time fields
#    'created', 'modified',
    # Product fields
    'product_oid',
    # ProductImage fields
    'is_primary_image', 'image_url'
)

# Lambda Handlers

@tracker
def api_handler(
    event: LambdaProxyInput, context: LambdaContext
) -> LambdaProxyOutput:
    """
    The read handler for product_images targets
    in the admin scope.

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
        _authnz_preflight()
        with tracker.timer('product_db_access'):
            product_images = ProductImage.get(
                db_source_name='ProductImages', **get_params
            )
        _authnz_reconcile()

        # Filter the results' fields
        results = [
            {
                key: value for key, value
                in product_image.model_dump(mode='json').items()
                if key in LIST_FIELD_NAMES
            }
            for product_image in product_images
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
def _authnz_preflight(*args, **kwargs):
    ...


def _authnz_reconcile(*args, **kwargs):
    ...


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
