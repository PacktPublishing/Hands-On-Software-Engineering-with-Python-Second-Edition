#!/usr/bin/env python3.11
"""
A minimal example application example, including a bare-
bones website and an API to show how Flask can integrate
with the HMS code built so far in the book.

To run this application:
• Navigate to the flask-example directory in a
  terminal/console.
• Run `pipenv run flask --app src/app run`

Add --debug if desired to see debugging inormation

Environment:
------------
FLASK_RUN_HOST : IP address, defaults to 127.0.0.1
    The IP address that the application is accessible at.
FLASK_RUN_PORT : str (numeric), defaults to 5000
    The port that the application is accessible at.
"""

from __future__ import annotations

# Built-In Imports
import json
import logging
import os
import pprint

# Third-Party Imports
from flask import Flask, render_template, request
from markupsafe import escape

# Path-Manipulations (avoid these!) and "Local" Imports
from hms.core.business_objects import Artisan, Address
from hms.core.data_objects import BaseDataObject

# Module "Constants" and Attributes
app = Flask(__name__)

# Set up local logging to console
logger = logging.getLogger(app.name)
formatter = logging.Formatter(
    f'[{app.name}] [%(levelname)-5.5s]  %(message)s'
)
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
logger.setLevel(
    os.getenv('FLASK_LOG_LEVEL', 'INFO').upper()
)

host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
port = os.getenv("FLASK_RUN_PORT", "5000")

logger.info(f'Starting {app.name} on http://{host}:{port}')
for key, value in os.environ.items():
    if key.startswith('MYSQL_') or key.startswith('DEV_') \
            or key.startswith('FLASK_'):
        logger.info(f'{key} '.ljust(24, '.') + f' {value}')

@app.route('/')
def website_home():
    initial_vars = vars()
    request_members = [
        name for name in dir(request)
        if not name.startswith('_')
    ]
    list_chunk_size = int(len(request_members)/3)
    base_dir = dir(BaseDataObject)
    artisan_fields = {
        f'artisan.{field_name}': {
            'required': getattr(field, 'required', False),
            'title': field.title,
            'description': field.description,
        }
        for field_name, field
        in Artisan.model_fields.items()
        if field_name not in base_dir
        and field_name not in ('business_address', 'products')
    }
    address_fields = {
        f'artisan.business_address.{field_name}': {
            'required': getattr(field, 'required', False),
            'title': field.title,
            'description': field.description,
        }
        for field_name, field
        in Address.model_fields.items()
        if field_name not in base_dir
    }
    artisan_fields.update(address_fields)

    context = {
        'page_title': 'Flask Example (simple application with API calls)',
        'vars': json.dumps(initial_vars, indent=4),
        'request': repr(request),
        'request_members': [
            request_members[i:i + list_chunk_size]
            for i in range(
                0, len(request_members),
                list_chunk_size
            )
        ],
        'artisan_fields': artisan_fields
    }
    return render_template('main.html', **context)

@app.route('/api/v1/')
def api_root():
    return f"""
<h1>api_root</h1>
<p><code>vars()</code></p>
<pre>{pprint.pformat(vars())}</pre>
<p><code>request</code></p>
<pre>{escape(repr(request))}</pre>
"""


@app.route('/api/v1/artisans/', methods=['GET'])
def get_artisans_root():
    try:
        artisans = Artisan.get(db_source_name='Artisan')
        results = [
            artisan.model_dump(mode='json')
            for artisan in artisans
        ]
        return json.dumps(results), 200
    except Exception as error:
        result = {
            'error': error.__class__.__name__,
            'details': str(error)
        }
        logger.exception(
            f'{error.__class__.__name__} encountered in '
            f'get_artisans_root: {error}'
        )
        return json.dumps(result), 500


@app.route('/api/v1/artisans/', methods=['POST'])
def post_artisans_root():
    # Added JS form submission
    payload = json.loads(request.data)
    logger.info(f'payload: {payload}')
    new_artisan = Artisan(**payload)
    logger.info(f'Created Artisan {new_artisan}')
    new_artisan.save(db_source_name='Artisan')
    return new_artisan.model_dump(mode='json'), 200


@app.route('/api/v1/artisans/<oid>/', methods=['GET'])
def get_artisan_by_oid(*args, **kwargs):
    logger.info(vars())
    try:
        artisans = Artisan.get(kwargs['oid'], db_source_name='Artisan')
        results = [
            artisan.model_dump(mode='json')
            for artisan in artisans
        ]
        return json.dumps(results), 200
    except Exception as error:
        result = {
            'error': error.__class__.__name__,
            'details': str(error)
        }
        logger.exception(
            f'{error.__class__.__name__} encountered in '
            f'get_artisans_root: {error}'
        )
        return json.dumps(result), 500

@app.route('/api/v1/artisans/<oid>/', methods=['PATCH'])
def patch_artisan_by_oid(*args, **kwargs):
    payload = json.loads(request.data)
    logger.info(f'payload: {payload}')
    artisan = Artisan.get(kwargs['oid'], db_source_name='Artisan')[0]
    logger.info(f'Retrieved Artisan {artisan}')
    try:
        for key, value in payload.items():
            if key == 'business_address':
                setattr(artisan, key, Address(**value))
            else:
                setattr(artisan, key, value)
        result = artisan.model_dump(mode='json')
        artisan.save(db_source_name='Artisan')
        status = 200
    except Exception as error:
        result = {
            'error': error.__class__.__name__,
            'details': str(error)
        }
        logger.exception(
            f'{error.__class__.__name__} encountered in '
            f'get_artisans_root: {error}'
        )
        status = 500
    return result, status
