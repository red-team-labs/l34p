#!/usr/bin/python


# l34p
# By: R4v3N
# Top-Hat-Sec <> Red|Team|Labs


import requests
import re
import sys
import random
from bs4 import BeautifulSoup



wordlist = 'NAMES.DIC'
uastring = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 
 }
base = 'http://www.screenleap.com/'
  

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def main():

    questiona = raw_input('Would you like to use a custom wordlist? ')

    if questiona:

        if questiona == 'y' or questiona == 'Y' or questiona == 'Yes' or questiona == 'yes':
            wordlist = raw_input('Enter Wordlist Name: ')
            f = open(wordlist)
        else:
            wordlist = 'NAMES.DIC'
            f = open(wordlist)
            
    for lineitem in iter(f):
        sanline = lineitem.rstrip()
        linkz = base+sanline
        #print 'Checking: '+linkz
        
        request = requests.get(linkz, headers=uastring, allow_redirects=True)
    
        # If you want to see if you are being redirected, uncomment the lines below
        #request.history
    
        #for req in request.history:
        #    print req.status_code, req.url
    
        c = request.content
        soup = BeautifulSoup(c)

        #Possible HTML can contain the following:

        rematch = re.findall(r'does not exist', str(soup))
        isoffline = re.findall(r'is not currently broadcasting', str(soup))
        isinvalid = re.findall(r'that is invalid', str(soup))

        
        #Check to see if above HTML finds were found, and if so, what to do:

        if rematch or isinvalid:
   
            print bcolors.FAIL + '[!] '+sanline+' Does not exist\n' + bcolors.ENDC
                
        else:

            print bcolors.OKBLUE + '[*] I Found Something! --> '+linkz+bcolors.ENDC
            with open('log.txt', 'a') as outfile:
                outfile.write(linkz+'\n')
                outfile.close()
            
            if isoffline:
            
                print '[*] '+sanline+' Is Not Broadcasting\n'
            
            else:
                
                # I have not tested what a broadcasting page contains since we do not have a java plugin running in requests but we can assume that a user is broadcasting
                
                print bcolors.OKGREEN + '[*] '+sanline+' MAY Be Broadcasting!\n' + bcolors.ENDC


if __name__ == '__main__':
    main()
