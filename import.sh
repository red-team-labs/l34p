#!/bin/bash

#l34p Import

#Use this script to import a list of valid screenleap links users as a wordlist.
#It will take a list that contains http://www.screenleap.com/testing and put testing into an import.txt file.
#you can then run l34p using import.txt


echo ''
read -p '[*] Enter List Of Links To Import: ' VALA

while read line; do

	echo $line | cut -d '/' -f4 >> imported.txt

done < $VALA

echo "[*] All Done."
