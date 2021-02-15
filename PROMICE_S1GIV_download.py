# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, GEUS (Geological Survey of Denmark and Greenland)

"""

import numpy as np
import urllib.request
import os
from multiprocessing import Pool, freeze_support
import time
import requests
from bs4 import BeautifulSoup
import re
import progressbar

# set path to store data
out_path = 'path/to/PROMICE_ice_velocity_data/'

# access website
response = requests.get('https://promice.org/PromiceDataPortal/api/' +
                        'download/92ce7cf4-59b8-4a3f-8f75-93d166f5a7ca/Greenland_IV')

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
    

def PROMICE_download(k):
          
    a_tag = a_tags[k]
    link = a_tag['href']
                
    # download file path
    download_url = 'https://promice.org/' + link
    urllib.request.urlretrieve(download_url, out_path + link.split('/')[-1],
                               MyProgressBar())
            
    print(k, 'Downloading %s' % download_url)
    
    

if __name__ == '__main__':

    freeze_support()
    
    nb_cores = 5
    
    start_time = time.time()
    start_local_time = time.ctime(start_time)
    
    with Pool(nb_cores) as p:
        p.map(PROMICE_download, np.arange(0, len(a_tags)))
        
    end_time = time.time()
    end_local_time = time.ctime(end_time)
    processing_time = (end_time - start_time) / 60
    print("--- Processing time: %s minutes ---" % processing_time)
    print("--- Start time: %s ---" % start_local_time)
    print("--- End time: %s ---" % end_local_time)
