l34p
Screenleap brute forcer

Screenleap or http://www.screenleap.com is a company that offers browser-based screenshare services. They have free
accounts and pro accounts. I have used them many times for quick demonstrations and even teaching classes and they
do have a great easy service. There is one thing that has always been on my mind though and that is the ease of
viewing other peoples screenshares. They do offer private screenshares however its a separate process and most people
just click a "Share Screen" button which shares their screen. By doing this, all a person has to know is either a 9 digit
screenshare code, or your account name. With no password protection at all, anyone with the link can view your screen,
invited OR uninvited. 

This brings us to this tool 'l34p'. It currently uses a default wordlist that contain names and checks screenleap to see
if they are valid accounts. If the account is valid, it will be stored in a log file. It goes one step further in attempting
to see if the user of that account is currently broadcasting. It outputs the status of everything for you to see.
It is not a finished project so there are some things that I will be working on over time.



DEPENDENCIES:

Python 2.7

The script uses the following libraries that can be installed via pip.

requests
BeautifulSoup4



USAGE:

python l34p.py or sudo python l34p.py
