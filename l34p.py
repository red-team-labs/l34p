#!/usr/bin/python

import requests
import re
from bs4 import BeautifulSoup


num_lines = sum(1 for line in open('NAMES.DIC'))
cur_lines = 0
wordlist = 'NAMES.DIC'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1' }
url = 'http://www.screenleap.com/'

with open(wordlist) as l:
    for line in l:
        linkz = url+line
        print 'Checking: '+linkz
        request = requests.get(linkz, headers)
        c = request.content
        soup = BeautifulSoup(c)

        #print soup
        #print request.status_code

        rematch = re.findall(r'does not exist', str(soup))

        if rematch:
        
            print '[!] Does not exist'
    
        else:
        
            print '[*] I Found Something! --> '+linkz
            print '[*] Checking If Live...'
            isoffline = re.findall(r'is not currently broadcasting', str(soup))
            print isoffline
 
            if not isoffline:  
                print '[*] User Is Offline'
            else:
                print '[**] User Is Online [**]'
        debugz = raw_input('')
