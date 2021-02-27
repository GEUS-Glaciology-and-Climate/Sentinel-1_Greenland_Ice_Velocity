# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, GEUS (Geological Survey of Denmark and Greenland)

"""

import numpy as np
import urllib.request
import os
import time
import requests
from bs4 import BeautifulSoup
import re
import progressbar
import argparse

# parse command-line arguments
parser = argparse.ArgumentParser(description='Download of the PROMICE Ice Velocity')

parser.add_argument('-i', help='Path of the website from where outputs'
                    + ' will be downloaded')
parser.add_argument('-o', help='Path of the folder where outputs will' 
                    + 'be stored')

args = parser.parse_args()
download_path = args.i
out_path = args.o

# access website
response = requests.get(download_path)

# parse html
soup = BeautifulSoup(response.text, 'html.parser')

# extract nc file hyperlinks
a_tags = soup.findAll('a', string=re.compile('nc'), recursive=True)
    

class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()
    

def PROMICE_download(a_tag): 
          
    link = a_tag['href']
                
    # download file path
    download_url = 'https://promice.org/' + link
    print('Downloading %s' % download_url)
    urllib.request.urlretrieve(download_url, out_path + link.split('/')[-1],
                               MyProgressBar())
    

start_time = time.time()
start_local_time = time.ctime(start_time)

for a_tag in a_tags:
    
    PROMICE_download(a_tag)
        
end_time = time.time()
end_local_time = time.ctime(end_time)
processing_time = (end_time - start_time) / 60
print("--- Processing time: %s minutes ---" % processing_time)
print("--- Start time: %s ---" % start_local_time)
print("--- End time: %s ---" % end_local_time)
