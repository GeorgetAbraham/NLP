#!/usr/bin/python
#
# Public domain software written by Arun Sharma (arun@sharma-home.net)
# 
# Converts iscii2itrans (or pseudo itrans)
#
# http://www.mit.gov.in/tdil/standards.htm
# http://www.aczone.com/itrans/

import sys, string

dict = { \
0xa1        : "an",
0xa2        : "am",
0xa3        : "aha",
0xa4        : "a",
0xa5        : "A",
0xa6        : "i",
0xa7        : "I",
0xa8        : "u",
0xa9        : "U",
0xaa        : "ru",
0xab        : "e",
0xac        : "E",
0xad        : "ai",
0xae        : "??",
0xaf        : "o",
0xb0        : "O",
0xb1        : "au",
0xb2        : "??",
0xb3        : "ka",
0xb4        : "kha",
0xb5        : "ga",
0xb6        : "gha",
0xb7        : "nga",
0xb8        : "cha",
0xb9        : "Cha",
0xba        : "ja",
0xbb        : "Jha",
0xbc        : "nya",
0xbd        : "Ta",
0xbe        : "Tha",
0xbf        : "Da",
0xc0        : "Dha",
0xc1        : "Na",
0xc2        : "ta",
0xc3        : "tha",
0xc4        : "da",
0xc5        : "dha",
0xc6        : "na",
0xc7        : "??",
0xc8        : "pa",
0xc9        : "pha",
0xca        : "ba",
0xcb        : "bha",
0xcc        : "ma",
0xcd        : "ya",
0xce        : "yya",
0xcf        : "ra",
0xd0        : "rra",
0xd1        : "la",
0xd2        : "La",
0xd3        : "??",
0xd4        : "va",
0xd5        : "sha",
0xd6        : "ssa",
0xd7        : "sa",
0xd8        : "ha",
0xd8        : "-arka-",
0xda        : "A",
0xdb        : "i",
0xdc        : "I",
0xdd        : "u",
0xde        : "U",
0xdf        : "Ru",
0xe0        : "e",
0xe1        : "E",
0xe2        : "AI",
0xe3        : "??",
0xe4        : "o",
0xe5        : "O",
0xe6        : "au",
0xe7        : "O",
0xe8        : "-1",
0xe9        : "??",
0xea        : "a"
}

try:
    files = map(open, sys.argv[1:])
except:
    files = [sys.stdin]

if len(files) == 0:
    files = [sys.stdin]

for file in files:
    d = file.read()
    ret = ""
    for c in d:
        try:
            o = ord(c)
            ch =  dict[o]
            if ch == "-1":
                ret = ret[:-1]
            elif o > 0xda and o < 0xe7:
                ret = ret[:-1] + ch
            else:
                ret = ret + ch
        except KeyError:
            ret = ret + c
    print ret
    
