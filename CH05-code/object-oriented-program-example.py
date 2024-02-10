#!/usr/bin/env python
"""
An example of a simple OOP-based program. Asks the user for a URL,
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


# Defining the class
class PageReader:
    # Object-initialization method
    def __init__(self, url):
        self.url = url
        url_characters = ''.join(
            [c for c in url if c not in ':/']
        )
        self.local_file = f'{tmp_dir}{url_characters}.data' \
            .replace('https', '').replace('http', '')
        self.page_data = self.get_page_data()

    # Method to read the data from the URL
    def get_page_data(self):
        page = urllib.request.urlopen(self.url)
        page_data = page.read()
        page.close()
        return page_data

    # Method to save the page-data
    def save_page_data(self):
        with open(self.local_file, 'w') as out_file:
            out_file.write(str(self.page_data))
            print('Page-data written to %s' % (self.local_file))


if __name__ == '__main__':
    print('Object-oriented code example')
    # Almost the same loop...
    the_url = ''
    while the_url.lower() != 'x':
        the_url = input(
            'Please enter a URL to read, or "X" to cancel: '
        )
        if the_url and the_url.lower() != 'x':
            page_reader = PageReader(the_url)
            page_reader.save_page_data()
    print('Exiting. Thanks!')
