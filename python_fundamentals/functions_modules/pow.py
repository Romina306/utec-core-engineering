#!/usr/bin/env python3


def pow(a, b):
    if b == 0:
        return 1

    negative_exponent = False
    if b < 0:
        negative_exponent = True
        b = abs(b)

    result = 1
    for _ in range(b):
        result *= a

    if negative_exponent:
        return 1 / result

    return result
