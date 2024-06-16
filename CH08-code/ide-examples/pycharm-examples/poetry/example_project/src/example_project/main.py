#!/usr/bin/env python3.11
"""
A bare-bones project module. All this module does is print that
it's being run, this docstring, and the interpreter that it's
running under.
"""

import os
import platform

import requests

CONSTANT='CONSTANT'

if __name__ == '__main__':
    from shutil import which
    interpreter = which('python')
    print(f'Running {__file__}')
    print('Example using {PACKAGE_MANAGER} in {IDE}'.format(**os.environ))
    print(f'The requests module: {requests}')
    print(__doc__)
    print(f'Project Python interpreter: {interpreter}')

    if platform.system() == 'Windows':
        input('Run completed without error. Press [Enter] to continue')
