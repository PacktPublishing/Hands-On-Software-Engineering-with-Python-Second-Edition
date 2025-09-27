import logging

import os, json, pymysql
import boto3

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_db_credentials():
    logger.info('Calling get_db_credentials')
    secrets = boto3.client('secretsmanager')
    logger.info(f'Got secretsmanager client {secrets}')
    secret_arn = os.environ['DB_SECRET_NAME']
    logger.info(f'Looking up secret at {secret_arn}')
    resp = secrets.get_secret_value(SecretId=secret_arn)
    logger.info(
        'Got secrets from ' + os.environ['DB_SECRET_NAME']
    )
    return json.loads(resp['SecretString'])


def lambda_handler(event, context):
    logger.info('Calling lambda_handler')
    creds = get_db_credentials()
    logger.info(
        'Making database connection to '
        + os.environ['DB_ENDPOINT']
    )
    conn = pymysql.connect(
        host=os.environ['DB_ENDPOINT'],
        port=int(os.environ['DB_PORT']),
        user=creds['username'],
        password=creds['password'],
        connect_timeout=5
    )
    query = 'SELECT schema_name ' \
        'FROM information_schema.SCHEMATA;'
    logger.info(f'Running query {query}')
    with conn.cursor() as cur:
        cur.execute(query)
        logger.info('Query executed')
        databases = cur.fetchall()
        logger.info('Data fetched')
    conn.close()
    logger.info('Connection closed')
    return {
        'statusCode': 200,
        'databases': str(databases)
    }

