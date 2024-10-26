#!/usr/bin/env python3.11
"""
Generates the OAS specification for the API that relates
to the hms.backend.api namespace in this project
structure.
"""
import os

from pathlib import Path

import yaml

from openapi_pydantic import \
    OpenAPI, Info, PathItem, Operation, Response
from openapi_pydantic.util import PydanticSchema, \
    construct_open_api_with_schema_class

from hms.artisan.objects import Artisan

api_definition = OpenAPI(
    info=Info(
        title='HMS Back-end API',
        version='2.0.0'
    ),
    paths={
        # API paths for Artisans to work with their data
        '/v1/artisan': PathItem(
            # Create
            # post=Operation(),
            # Read
            get=Operation(
                responses={
                    '200': Response(
                        description='The complete Artisan data',
                        content={
                            'application/json': {
                                'schema': PydanticSchema(schema_class=Artisan)
                            }
                        }
                    )
                },
            ),
            # Update
            # put=Operation(),
            # Delete
            # delete=Operation(),
        ),
    }
)

openapi_definition = construct_open_api_with_schema_class(
    api_definition
)

open_api_yaml = yaml.dump(
    openapi_definition.model_dump(
        mode='json', by_alias=True, exclude_none=True
    ),
    default_flow_style=False
)

open_api_file = Path(__file__).parent.parent / 'docs' / 'oas.yaml'
open_api_file.write_text(open_api_yaml)

script_name = __file__.split(os.sep)[-1].split(os.extsep)[0]
raise NotImplementedError(
    f'The {script_name} script is not complete yet!\n'
    f'The documentation generated at {open_api_file.name} '
    'is INCOMPLETE, and should not be used for production '
    'implementation or planning!'
)
