import logging
import os

if 'logger' not in globals():
    logger = logging.getLogger()
    logger.setLevel(
        os.getenv('LOG_LEVEL', 'INFO').upper()
    )
