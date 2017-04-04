#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Marcus Botacin - 2017

import sys

alphabet={
            'A':'Alpha',
            'B':'Bravo',
            'C':'Charlie',
            'D':'Delta',
            'E':'Echo',
            'F':'Foxtrot',
            'G':'Golf',
            'H':'Hotel',
            'I':'India',
            'J':'Juliett',
            'K':'Kilo',
            'L':'Lima',
            'M':'Mike',
            'N':'November',
            'O':'Oscar',
            'P':'Papa',
            'Q':'Quebec',
            'R':'Romeo',
            'S':'Sierra',
            'T':'Tango',
            'U':'Uniform',
            'V':'Victor',
            'W':'Whiskey',
            'X':'Xray',
            'Y':'Yankee',
            'Z':'Zulu',
            '0':'Zero',
            '1':'One',
            '2':'Two',
            '3':'Three',
            '4':'Four',
            '5':'Five',
            '6':'Six',
            '7':'Seven',
            '8':'Eight',
            '9':'Nine'
}

# Usage message
def usage(name):
    print("./%s -e '<text to encode>'" % name)
    print("./%s -d '<text to decode>'" % name)

# encode into phonetic
def encode(text):
    phrase=[]
    for i in text:
	# only upper case
        c=i.upper()
	# - as separator
        if(c==" "):
            phrase.append("-")
	# char conversion
        elif(c in alphabet):
            phrase.append(alphabet[c])
    return " ".join(phrase)

# decode from phonetic
def decode(text):
    phrase=[]
    for i in text:
	# allowed separator
        if(i == "-"):
	    phrase.append(" - ")
	# char converter
	elif(i in alphabet):
            phrase.append(i)
    return "".join(phrase)


# Entry Point

if __name__ == "__main__":

	# bin_name + option + message
	if(len(sys.argv)!=3):
	    usage(sys.argv[0])
	elif(sys.argv[1]=="-e"):
	    print(encode(sys.argv[2]))
	elif(sys.argv[1]=="-d"):
	    print(decode(sys.argv[2]))
	else:
	    usage(sys.argv[0])
