#!/usr/bin/python

import requests
import re
import sys
from bs4 import BeautifulSoup


wordlist = 'NAMES.DIC'

useragent =  { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1' 
}

base = 'http://www.screenleap.com/'

debugz = [wordlist, useragent, base]
print debugz
debugz = raw_input('')

f = open(wordlist)
  
for lineitem in iter(f):
    sanline = lineitem.rstrip()
    linkz = base+sanline
    print 'Checking: '+linkz
    debugz = raw_input('')
    request = requests.get(linkz, headers=useragent, allow_redirects=True)
    request.history
    for req in request.history:
        print req.status_code, req.url
    debugz = raw_input('')
    print str(request.content)
    c = request.content
    soup = BeautifulSoup(c)

    print soup
    #debugz = raw_input('')
	#print request.status_code

    rematch = re.findall(r'does not exist', str(soup))
    isoffline = re.findall(r'is not currently broadcasting', str(soup))
    isinvalid = re.findall(r'that is invalid', str(soup))

        
    if rematch or isinvalid:
   
        print '[!] Does not exist'
        #debugz = raw_input('')
            
    else:

        print '[*] I Found Something! --> '+linkz
            
        if isoffline:
            
            print '[*] User Is Not Broadcasting'
            
        else:
            
            print '[*] User MAY Be Broadcasting!'
            
    debugz = raw_input('')
        
