#!/usr/bin/python3

def islower(c):
    n = ord(c)
    if n < 123 and n > 96:
        return True
    else:
        return False
