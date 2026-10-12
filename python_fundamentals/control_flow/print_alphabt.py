#!/usr/bin/env python3
alphabet = ""
for letra in range(ord('a'), ord('z') + 1):
    if chr(letra) != 'e' and chr(letra) != 'q':
        alphabet += chr(letra)

print("{}".format(alphabet))