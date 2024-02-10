#!/usr/bin/env python
"""
An example of a simple procedural program. Asks the user for a URL,
retrieves the content of that URL (http:// or https:// required),
writes it to a temp-file, and repeats until the user tells it to
stop.
"""

import os

import urllib.request

if os.name == 'posix':
    tmp_dir = '/tmp/'
else:
    tmp_dir = 'C:\\Temp\\'

print('Simple procedural code example')

the_url = ''
while the_url.lower() != 'x':
    the_url = input(
        'Please enter a URL to read, or "X" to cancel: '
    )
    if the_url and the_url.lower() != 'x':
        page = urllib.request.urlopen(the_url)
        page_data = page.read()
        page.close()
        local_file = ('%s%s.data' % (tmp_dir, ''.join(
            [c for c in the_url if c not in ':/']
            )
        )).replace('https', '').replace('http', '')
        with open(local_file, 'w') as out_file:
            out_file.write(str(page_data))
            print('Page-data written to %s' % (local_file))

print('Exiting. Thanks!')
