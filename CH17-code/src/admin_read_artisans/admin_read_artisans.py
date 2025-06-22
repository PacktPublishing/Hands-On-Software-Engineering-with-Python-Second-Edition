#!/usr/bin/env python3.11
"""
Provides the backing Lambda Function for the API endpoint
that handles read artisans functionality.
"""
from __future__ import annotations

# Built-In Imports
import json

from pathlib import Path

# Third-Party Imports
from hms.core.business_objects import Artisan

from awslambdaric.lambda_context import LambdaContext
from goblinfish.metrics.trackers import ProcessTracker

# Path Manipulations (avoid these!) and "Local" Imports
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
    'created', 'modified',
    # Person name fields
    'honorific',
    'given_name', 'middle_name', 'family_name',
    'suffix',
    # Company fields
    'company_name'
)

# Lambda Handlers

@tracker
def api_handler(
    event: LambdaProxyInput, context: LambdaContext
) -> LambdaProxyOutput:
    """
    The read handler for artisans targets
    in the admin scope.

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
        get_params = event.get('queryStringParameters', {})
        pagination_params = {
            key: int(get_params.get(key, 0)) or None
            for key in ('page_size', 'page_number')
        }
        get_params.update(pagination_params)
        logger.debug(f'get_params: {get_params}')

        # Get the Artisan objects, keeping track of how
        # long the process takes for metrics purposes
        with tracker.timer('artisan_db_access'):
            artisans = Artisan.get(
                db_source_name='Artisan', **get_params
            )

        # Filter the results' fields
        results = [
            {
                key: value for key, value
                in artisan.model_dump(mode='json').items()
                if key in LIST_FIELD_NAMES
            }
            for artisan in artisans
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
