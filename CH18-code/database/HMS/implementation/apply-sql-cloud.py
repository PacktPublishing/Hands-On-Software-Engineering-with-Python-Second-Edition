import getpass
import os
import sys

from datetime import datetime
from pathlib import Path
from subprocess import run

import pymysql

sql_files = sorted(Path(__file__).parent.glob('*.sql'))
if not sql_files:
    print('No SQL files found to execute')
    sys.exit()

# Get user and password info
password = os.getenv('MYSQL_MASTER_USER', None)
username = os.getenv('MYSQL_MASTER_PASS', None)

# Back the database up before touching it!
rds = boto3.client('rds')
backup_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_name = (
    os.environ['MYSQL_DB'] + f'_{backup_time}.backup'
).lower()
# Start the backup (snapshot)
snapshot_response = rds.create_db_snapshot(
    DBSnapshotIdentifier=backup_name,
    DBInstanceIdentifier=os.environ['MYSQL_INSTANCE_NAME'],
)
# Wait for it to complete
waiter = rds.get_waiter('db_snapshot_completed')
try:
    waiter.wait(
        DBSnapshotIdentifier=backup_name,
        # Check four times per minute,
        # for no more than 10 minutes
        WaiterConfig={
            'Delay': 15,
            'MaxAttempts': 40,
        }
    )
except Exception as error:
    print(
        f'{error.__class__.__name__} encountered while '
        'waiting for the snapshot of the database to '
        'complete.'
    )
    sys.exit(1)

# Connect to the database
with pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    port=os.environ['MYSQL_PORT'],
    database=os.environ['MYSQL_DB'],
    user=username,
    password=password
) as db:
    print(
        f'Connection to {db.database} database '
        f'at {db.server_host} as {username} made'
    )
    # Run all the files
    for number, sql_file in enumerate(sql_files):
        sql = sql_file.read_text().format(**os.environ)
        print(f'{number+1:>4} {sql_file.name}')
        try:
            with db.cursor() as cursor:
                cursor.execute(sql)
                db.commit()
        except mysql.connector.Error as err:
            if err.errno == -1:
                pass
            else:
                print(err)
                print(err.errno)

db.close()
