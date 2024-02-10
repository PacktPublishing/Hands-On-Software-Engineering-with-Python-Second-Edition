#!/usr/bin/env python
"""
An example of a simple FP-based program. Asks the user for a URL, 
retrieves the content of that URL, writes it to a temp-file, and 
repeats until the user tells it to stop.
"""

# Importing stuff we'll use
import os

import urllib.request

if os.name == 'posix':
    tmp_dir = '/tmp/'
else:
    tmp_dir = 'C:\\Temp\\'
if not os.path.exists(tmp_dir):
    os.mkdirs(tmp_dir)

# Defining our functions

def get_page_data(url):
    page = urllib.request.urlopen(url)
    page_data = page.read()
    page.close()
    return page_data

def save_page_data(local_file, page_data):
    with open(local_file, 'w') as out_file:
        out_file.write(str(page_data))
        return('Page-data written to %s' % (local_file))

def get_local_file_path(url):
  return ('%s%s.data' % (tmp_dir, ''.join(
      [c for c in the_url if c not in ':/']
      )
    )).replace('https', '').replace('http', '')

def process_page(url):
    return save_page_data(
        get_local_file_path(url), get_page_data(url)
    )

def get_page_to_process():
    the_url = input(
        'Please enter a URL to read, or "X" to cancel: '
    )
    if the_url:
        return the_url.lower()
    return None

if __name__ == '__main__':
    print('Functional Programming code example')
    # Again, almost the same loop...
    the_url = get_page_to_process()
    while the_url not in ('x', None):
        print(process_page(the_url))
        the_url = get_page_to_process()
    print('Exiting. Thanks!')
