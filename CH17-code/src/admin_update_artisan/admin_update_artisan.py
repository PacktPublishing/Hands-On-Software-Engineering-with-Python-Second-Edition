#!/usr/bin/env python3.11
"""
Provides the backing Lambda Function for the API endpoint
that handles update artisan functionality.
"""
from __future__ import annotations

# Built-In Imports
import json

from pathlib import Path

# Third-Party Imports
from hms.core.business_objects import Artisan, \
    ArtisanNotFoundError

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
    The update handler for artisan targets
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

        # Get the oid of the Artisan to be updated
        artisan_oid = event.get(
            'pathParameters', {}
        ).get('oid')
        if artisan_oid is None \
                or len(artisan_oid.split(',')) != 1:
            raise ValueError(
                f'{module}.api_handler requires a single '
                'oid, but that path parameter resolved to '
                f'"{artisan_oid}" ({type(artisan_oid).__name__}).'
            )

        # Retrieve the payload from event['body']
        body = payload = json.loads(
            event.get('body', 'null')
        )
        logger.debug(f'payload: {json.dumps(payload)}')

        if payload is None:
            raise ValueError(
                f'{module}.api_handler expects one or '
                'more allowed fields with values to '
                'update, but none were supplied.'
            )

        # Check for allowed fields in the update request
        allowed_fields = {'is_active', 'is_deleted'}
        payload = {
            key: payload[key] for key in allowed_fields
            if key in payload
        }
        if not payload:
            raise ValueError(
                f'{module}.api_handler expects one or '
                'more allowed fields '
                f'{tuple(allowed_fields)} with values'
                ' to update, but none were supplied.'
            )

        # If the request has fields that are not
        # allowed, raise an error
        requested_fields = set(body.keys())
        logger.debug(
            f'requested_fields: {requested_fields}'
        )
        forbidden_fields = requested_fields.difference(
            allowed_fields
        )
        logger.debug(
            f'forbidden_fields: {forbidden_fields}'
        )
        if forbidden_fields:
            raise ValueError(
                f'{module}.api_handler was passed '
                f'{tuple(forbidden_fields)} fields, '
                'which are not allowed in an update.'
            )

        # Retrieve the current Artisan and convert
        # it to a dict
        with tracker.timer('artisan_db_read_access'):
            artisans = Artisan.get(
                artisan_oid, db_source_name='Artisan'
            )
        # Raise an error if no Artisan could be found
        if len(artisans) == 0:
            raise ArtisanNotFoundError(
                'Could not retrieve an Artisan '
                f'identified by "{artisan_oid}".'
            )
        artisan_data = artisans[0].model_dump(mode='json')
        logger.debug(
            f'Unmodified Artisan {artisan_oid}: '
            f'{json.dumps(artisan_data)}'
        )
        # Update that dict with the payload values
        artisan_data.update(payload)
        logger.debug(
            f'Modified Artisan {artisan_oid}: '
            f'{json.dumps(artisan_data)}'
        )
        # Create a new Artisan instance with the
        # updated data and save it
        updated_artisan = Artisan(**artisan_data)
        with tracker.timer('artisan_db_write_access'):
            updated_artisan.save(db_source_name='Artisan')

        result = {
            'statusCode': 200,
            'body': json.dumps(
                updated_artisan.model_dump(mode='json')
            )
        }

    except ArtisanNotFoundError as error:
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

    except ValueError as error:
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
