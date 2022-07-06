#!/usr/bin/python3
def getInt(c):
    rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    val = [1, 5, 10, 50, 100, 500, 1000]
    return val[rom.index(c)]


def roman_to_int(roman_string):
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
