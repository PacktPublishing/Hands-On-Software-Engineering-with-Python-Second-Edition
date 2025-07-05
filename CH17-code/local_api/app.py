#!/usr/bin/env python3.11
"""
Local

Usage:
------
From the project root directory (where the Pipfile is),
run:

pipenv run uvicorn local_api.app:app --port 5000 --reload
"""

import logging
import sys

from os import sep, extsep

from pathlib import Path

# Path Manipulations (avoid these!) and "Local" Imports

# These are apparently needed by FastAPI?

# Add main Lambdas logging, and
# output in FastAPI app context
from logger import logger
formatter = logging.Formatter(
    "[%(levelname)s]  %(message)s"
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

from goblinfish.aws.local.api_gateway.fastapi import (
    FastAPI, Request
)

app = FastAPI()

# (admin create artisan)
app.post(
    '/api/v1/admin/artisan/{oid}/',
    'admin_create_artisan.admin_create_artisan.api_handler'
)()

# (admin create product)
app.post(
    '/api/v1/admin/product/{oid}/',
    'admin_create_product.admin_create_product.api_handler'
)()

# (admin create product_image)
app.post(
    '/api/v1/admin/product_image/{oid}/',
    'admin_create_product_image.admin_create_product_image.api_handler'
)()

# (admin delete artisan)
app.delete(
    '/api/v1/admin/artisan/{oid}/',
    'admin_delete_artisan.admin_delete_artisan.api_handler'
)()

# (admin delete product)
app.delete(
    '/api/v1/admin/product/{oid}/',
    'admin_delete_product.admin_delete_product.api_handler'
)()

# (admin delete product_image)
app.delete(
    '/api/v1/admin/product_image/{oid}/',
    'admin_delete_product_image.admin_delete_product_image.api_handler'
)()

# (admin read artisan)
app.get(
    '/api/v1/admin/artisan/{oid}/',
    'admin_read_artisan.admin_read_artisan.api_handler'
)()

# (admin read artisans)
app.get(
    '/api/v1/admin/artisans/',
    'admin_read_artisans.admin_read_artisans.api_handler'
)()

# (admin read product)
app.get(
    '/api/v1/admin/product/{oid}/',
    'admin_read_product.admin_read_product.api_handler'
)()

# (admin read product_image)
app.get(
    '/api/v1/admin/product_image/{oid}/',
    'admin_read_product_image.admin_read_product_image.api_handler'
)()

# (admin read product_images)
app.get(
    '/api/v1/admin/product_images/',
    'admin_read_product_images.admin_read_product_images.api_handler'
)()

# (admin read products)
app.get(
    '/api/v1/admin/products/',
    'admin_read_products.admin_read_products.api_handler'
)()

# (admin update artisan)
app.patch(
    '/api/v1/admin/artisan/{oid}/',
    'admin_update_artisan.admin_update_artisan.api_handler'
)()

# (admin update product)
app.patch(
    '/api/v1/admin/product/{oid}/',
    'admin_update_product.admin_update_product.api_handler'
)()

# (admin update product_image)
app.patch(
    '/api/v1/admin/product_image/{oid}/',
    'admin_update_product_image.admin_update_product_image.api_handler'
)()

# (artisan create artisan)
app.post(
    '/api/v1/artisan/{artisan_oid}/artisan/{oid}/',
    'artisan_create_artisan.artisan_create_artisan.api_handler'
)()

# (artisan create product)
app.post(
    '/api/v1/artisan/{artisan_oid}/product/{oid}/',
    'artisan_create_product.artisan_create_product.api_handler'
)()

# (artisan create product_image)
app.post(
    '/api/v1/artisan/{artisan_oid}/product_image/{oid}/',
    'artisan_create_product_image.artisan_create_product_image.api_handler'
)()

# (artisan delete artisan)
app.delete(
    '/api/v1/artisan/{artisan_oid}/artisan/{oid}/',
    'artisan_delete_artisan.artisan_delete_artisan.api_handler'
)()

# (artisan delete product)
app.delete(
    '/api/v1/artisan/{artisan_oid}/product/{oid}/',
    'artisan_delete_product.artisan_delete_product.api_handler'
)()

# (artisan delete product_image)
app.delete(
    '/api/v1/artisan/{artisan_oid}/product_image/{oid}/',
    'artisan_delete_product_image.artisan_delete_product_image.api_handler'
)()

# (artisan read artisan)
app.get(
    '/api/v1/artisan/{artisan_oid}/artisan/{oid}/',
    'artisan_read_artisan.artisan_read_artisan.api_handler'
)()

# (artisan read artisans)
app.get(
    '/api/v1/artisan/{artisan_oid}/artisans/',
    'artisan_read_artisans.artisan_read_artisans.api_handler'
)()

# (artisan read product)
app.get(
    '/api/v1/artisan/{artisan_oid}/product/{oid}/',
    'artisan_read_product.artisan_read_product.api_handler'
)()

# (artisan read product_image)
app.get(
    '/api/v1/artisan/{artisan_oid}/product_image/{oid}/',
    'artisan_read_product_image.artisan_read_product_image.api_handler'
)()

# (artisan read product_images)
app.get(
    '/api/v1/artisan/{artisan_oid}/product_images/',
    'artisan_read_product_images.artisan_read_product_images.api_handler'
)()

# (artisan read products)
app.get(
    '/api/v1/artisan/{artisan_oid}/products/',
    'artisan_read_products.artisan_read_products.api_handler'
)()

# (artisan update artisan)
app.patch(
    '/api/v1/artisan/{artisan_oid}/artisan/{oid}/',
    'artisan_update_artisan.artisan_update_artisan.api_handler'
)()

# (artisan update product)
app.patch(
    '/api/v1/artisan/{artisan_oid}/product/{oid}/',
    'artisan_update_product.artisan_update_product.api_handler'
)()

# (artisan update product_image)
app.patch(
    '/api/v1/artisan/{artisan_oid}/product_image/{oid}/',
    'artisan_update_product_image.artisan_update_product_image.api_handler'
)()

# (public create artisan)
app.post(
    '/api/v1/artisan/',
    'public_create_artisan.public_create_artisan.api_handler'
)()

# (public create product)
app.post(
    '/api/v1/product/{oid}/',
    'public_create_product.public_create_product.api_handler'
)()

# (public create product_image)
app.post(
    '/api/v1/product_image/{oid}/',
    'public_create_product_image.public_create_product_image.api_handler'
)()

# (public delete artisan)
app.delete(
    '/api/v1/artisan/{oid}/',
    'public_delete_artisan.public_delete_artisan.api_handler'
)()

# (public delete product)
app.delete(
    '/api/v1/product/{oid}/',
    'public_delete_product.public_delete_product.api_handler'
)()

# (public delete product_image)
app.delete(
    '/api/v1/product_image/{oid}/',
    'public_delete_product_image.public_delete_product_image.api_handler'
)()

# (public read artisan)
app.get(
    '/api/v1/artisan/{oid}/',
    'public_read_artisan.public_read_artisan.api_handler'
)()

# (public read artisans)
app.get(
    '/api/v1/artisans/',
    'public_read_artisans.public_read_artisans.api_handler'
)()

# (public read product)
app.get(
    '/api/v1/product/{oid}/',
    'public_read_product.public_read_product.api_handler'
)()

# (public read product_image)
app.get(
    '/api/v1/product_image/{oid}/',
    'public_read_product_image.public_read_product_image.api_handler'
)()

# (public read product_images)
app.get(
    '/api/v1/product_images/',
    'public_read_product_images.public_read_product_images.api_handler'
)()

# (public read products)
app.get(
    '/api/v1/products/',
    'public_read_products.public_read_products.api_handler'
)()

# (public update artisan)
app.patch(
    '/api/v1/artisan/{oid}/',
    'public_update_artisan.public_update_artisan.api_handler'
)()

# (public update product)
app.patch(
    '/api/v1/product/{oid}/',
    'public_update_product.public_update_product.api_handler'
)()

# (public update product_image)
app.patch(
    '/api/v1/product_image/{oid}/',
    'public_update_product_image.public_update_product_image.api_handler'
)()


if __name__ == '__main__':
    from pprint import pprint

    pprint(sorted(app.routes, key=lambda r: r.path))
