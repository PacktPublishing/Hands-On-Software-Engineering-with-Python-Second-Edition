#!/usr/bin/env python3.11

from __future__ import annotations

import logging
import os
import pprint

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from hms.core.business_objects import Artisan, Address
from hms.core.data_objects import BaseDataObject, \
    get_env_database_connector

host = os.getenv('FASTAPI_RUN_HOST', '127.0.0.1')
port = int(os.getenv('FASTAPI_RUN_PORT', '5000'))

app = FastAPI()

# Templates (Jinja2)
templates = Jinja2Templates(directory='templates')

# Static files
app.mount('/static', StaticFiles(directory='static'), name='static')

# Logging
logger = logging.getLogger('fastapi_app')
formatter = logging.Formatter('[%(name)s] [%(levelname)-5.5s] %(message)s')
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
logger.setLevel(os.getenv('FASTAPI_LOG_LEVEL', 'INFO').upper())

logger.info(f'Starting FastAPI app on http://{host}:{port}')
for key, value in os.environ.items():
    if key.startswith(('MYSQL_', 'DEV_', 'FASTAPI_')):
        logger.info(f'{key}'.ljust(24, '.') + f' {value}')


@app.get('/api/v1/')
async def api_root(request: Request):
    content = f"""<h1>api_root</h1>
<p><code>vars()</code></p>
<pre>{pprint.pformat(vars(request))}</pre>
<p><code>request</code></p>
<pre>{repr(request)}</pre>
"""
    return HTMLResponse(
        content=content,
        status_code=200
    )


@app.get('/api/v1/artisans/{oid}/')
async def get_artisan_by_oid(oid: str):
    try:
        get_env_database_connector()
        artisans = Artisan.get(
            oid, db_source_name='Artisan'
        )
        results = [
            artisan.model_dump(mode='json')
            for artisan in artisans
        ]
        return JSONResponse(content=results)
    except Exception as error:
        logger.exception('Error in get_artisan_by_oid')
        raise HTTPException(
            status_code=500, detail=str(error)
        )


@app.get('/api/v1/artisans/')
async def get_artisans_root():
    try:
        get_env_database_connector()
        artisans = Artisan.get(db_source_name='Artisan')
        results = [
            artisan.model_dump(mode='json')
            for artisan in artisans
        ]
        return JSONResponse(content=results)
    except Exception as error:
        logger.exception('Error in get_artisans_root')
        raise HTTPException(
            status_code=500, detail=str(error)
        )


@app.patch('/api/v1/artisans/{oid}/')
async def patch_artisan_by_oid(oid: str, payload: dict):
    try:
        get_env_database_connector()
        artisan = Artisan.get(
            oid, db_source_name='Artisan'
        )[0]
        logger.info(f'Retrieved Artisan {artisan}')
        for key, value in payload.items():
            if key == 'business_address':
                setattr(artisan, key, Address(**value))
            else:
                setattr(artisan, key, value)
        artisan.save(db_source_name='Artisan')
        return artisan.model_dump(mode='json')
    except Exception as error:
        logger.exception('Error in patch_artisan_by_oid')
        raise HTTPException(
            status_code=500, detail=str(error)
        )


@app.post('/api/v1/artisans/')
async def post_artisans_root(payload: dict):
    try:
        get_env_database_connector()
        new_artisan = Artisan(**payload)
        new_artisan.save(db_source_name='Artisan')
        return JSONResponse(
            content=new_artisan.model_dump(mode='json')
        )
    except Exception as error:
        logger.exception('Error in post_artisans_root')
        raise HTTPException(
            status_code=500, detail=str(error)
        )


@app.get('/', response_class=HTMLResponse)
async def website_home(request: Request):
    request_members = [
        name for name in dir(request)
        if not name.startswith('_')
    ]
    list_chunk_size = int(len(request_members) / 3)
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
        and field_name not in (
            'business_address', 'products'
        )
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

    return templates.TemplateResponse('main.html', {
        'request': request,
        'page_title': 'FastAPI Example '
        '(Containerized simple application with API calls)',
        'request_members': [
            request_members[i:i + list_chunk_size]
            for i in range(
                0, len(request_members),
                list_chunk_size
            )
        ],
        'artisan_fields': artisan_fields
    })
