#!/usr/bin/env python3.11
"""
Provides the backing Lambda Function for the API endpoint
that handles create artisan functionality.
"""
from __future__ import annotations

# Built-In Imports
import json

from pathlib import Path

# Third-Party Imports
from awslambdaric.lambda_context import LambdaContext
from goblinfish.metrics.trackers import ProcessTracker
from pydantic import ValidationError

# Path Manipulations (avoid these!) and "Local" Imports
from logger import logger

from hms.core.business_objects import Artisan

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
    The create handler for artisan targets
    in the public scope.

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
        artisan_data = json.loads(event['body'])
        new_artisan = Artisan(**artisan_data)
        new_artisan.save(db_source_name='Artisan')
        _authnz_reconcile()
        result = {
            'statusCode': 201,
            'body': new_artisan.model_dump_json()
        }

    except ValidationError as error:
        # Gather up the error information from
        # the Pydantic ValidationError
        invalid_fields = {
            '.'.join(invalid_field['loc']).split('[')[0]:
                invalid_field['msg']
            for invalid_field in error.errors()
        }
        # Standard error-logging
        logger.exception(
            f'{error.__class__.__name__}: {error} '
            'occured in api_handler'
        )
        logger.error(f'event: {json.dumps(event)}')
        logger.error(f'context: {repr(context)}')
        # Also log the fields that caused problems...
        logger.error(f'invalid_fields: {invalid_fields}')
        # ...and include them in the response:
        reponse_body = {
            'message': 'Bad Request: '
            f'({context.aws_request_id})',
            'fields': invalid_fields
        }
        result = {
            'statusCode': 400,
            'body': json.dumps(reponse_body)
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
