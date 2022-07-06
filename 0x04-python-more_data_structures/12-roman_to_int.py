#!/usr/bin/python3
def getInt(c):
    rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    val = [1, 5, 10, 50, 100, 500, 1000]
    return val[rom.index(c)]


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    pre = 0
    summ = 0
    rev = reversed(roman_string)
    for i, c in enumerate(rev):
        cur = getInt(c)
        v = len(roman_string) - 1
        if v - i == v:
            summ += cur
        else:
            if cur < pre:
                summ -= cur
            else:
                summ += cur
        pre = cur
    return summ
