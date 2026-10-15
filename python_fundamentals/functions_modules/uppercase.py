#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += "{0}".format(chr(ord(c) - 32))
        else:
            result += "{0}".format(c)
    print(result)



    