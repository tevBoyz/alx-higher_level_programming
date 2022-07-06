#!/usr/bin/python3
def getInt(c):
    rom = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return rom[c]


def roman_to_int(roman_string):
    if roman_string is None:
        return 0;
    pre = 0
    sum = 0
    rev = reversed(roman_string)
    for i, c in enumerate(rev):
        cur = getInt(c)
        v = len(roman_string) - 1
        if v - i == v:
            sum += cur
        else:
            if cur < pre:
                sum -= cur
            else:
                sum += cur
        pre = cur
    return sum   
