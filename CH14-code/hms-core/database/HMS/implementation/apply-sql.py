import getpass
import os
import sys

from datetime import datetime
from pathlib import Path
from subprocess import run

import mysql.connector

sql_files = sorted(Path(__file__).parent.glob('*.sql'))
if not sql_files:
    print('No SQL files found to execute')
    sys.exit()

# Get user and password info
password = os.getenv('DEV_PASS', None)
username = os.getenv('DEV_USER', None)

if username is None:
    default_user = getpass.getuser()
    user_prompt = f'Input your username [{default_user}]: '
    username = input(user_prompt) or default_user

if password is None:
    pass_prompt = 'Input your password to the ' \
        '{MYSQL_DB} database at {MYSQL_HOST}:\n> ' \
        .format(**os.environ)
    password = getpass.getpass(prompt=pass_prompt)

# Back the database up before touching it!
backup_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_name = os.environ['MYSQL_DB'] + f'_{backup_time}.backup'
backup_dir = Path(__file__).parent.parent / 'backups'
if not backup_dir.exists():
    backup_dir.mkdir()
backup_file = backup_dir / backup_name
backup_cmd = [
    'mysqldump',
    # Host, port, and database
    '-B', os.environ['MYSQL_DB'],
    '-h', os.environ['MYSQL_HOST'],
    # ~ '-P', os.environ['MYSQL_PORT'],
    # Access controls
    '-u', username,
    '-p',
]
display_backup_cmd = ' '.join(backup_cmd) \
    .replace(password, 'REDACTED')
print(f'== Backing the database up '.ljust(80, '='))
print(f'Running {display_backup_cmd}')
with open(backup_file, 'w') as f:
    run(backup_cmd, stdout=f)

# Connect to the database
with mysql.connector.connect(
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
        sql = sql_file.read_text()
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
