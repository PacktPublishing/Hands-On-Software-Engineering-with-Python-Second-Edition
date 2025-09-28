import os
from functools import cache

import boto3

from logger import logger

@cache
def get_env_vars(*names):
    logger.debug(f'Calling get_env_vars(*{names})')
    ssm = boto3.client('ssm')
    logger.debug('SSM client created')
    logger.debug(
        'Getting parameters on path '
        + os.environ['SERVICE_PARAMS_PATH']
    )
    parameters = ssm.get_parameters_by_path(
        Path=os.environ['SERVICE_PARAMS_PATH'],
        WithDecryption=True
    )['Parameters']
    logger.debug(
        f'Parameters retrieved ({len(parameters)})'
    )
    for parameter in parameters:
        name = parameter['Name'].split('/')[-1]
        if name in names:
            logger.debug(f'Setting os.environ["{name}"]')
            os.environ[name] = parameters['Value']
    logger.info(f'get_env_vars(*{names}) completed')
