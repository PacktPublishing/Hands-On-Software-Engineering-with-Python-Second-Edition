#!/usr/bin/env python3.11
"""
A script that runs pipenv check with a collection of
vulnerabilities to ignore, each of which is documented
with a reason in the script itself.

See example-scan-results.txt for details
"""
import os
import sys

from subprocess import run
from shutil import which

assert which('pipenv'), \
    f'{__file__.split(os.sep)[-1].split(os.extsep)[0]} ' \
    'requires an active pipenv environment, but the ' \
    'pipenv command could not be found.'

IGNORE_ITEMS = {
    # vulnerability_number: 'Reason to ignore it',

    # 39611: 'Not deployed to production, so not a '
    # 'critical issue'
}

command = ['pipenv', 'check'] + [
    f'-i {number}' for number in IGNORE_ITEMS
]

print(f'Running {" ".join(command)}')
sys.exit(run(' '.join(command), shell=True).returncode)
