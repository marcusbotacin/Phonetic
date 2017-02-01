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


def usage(name):
    print("./%s -e '<text to encode>'" % name)
    print("./%s -d '<text to decode>'" % name)

def encode(text):
    phrase=[]
    for i in text:
        c=i.upper()
        if(c==" "):
            phrase.append("-")
        elif(c in alphabet):
            phrase.append(alphabet[c])
    return " ".join(phrase)

def decode(text):
    phrase=[]
    for i in text:
        if(i == "-" or i in alphabet):
            phrase.append(i)
    return " ".join(phrase)


if(len(sys.argv)!=3):
    usage(sys.argv[0])
elif(sys.argv[1]=="-e"):
    print(encode(sys.argv[2]))
elif(sys.argv[1]=="-d"):
    print(decode(sys.argv[2]))
else:
    usage(sys.argv[0])
