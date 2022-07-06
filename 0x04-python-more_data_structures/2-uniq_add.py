#!/usr/bin/python3
def uniq_add(my_list=[]):
    ulist = set(my_list)
    sum = 0
    for i in ulist:
        sum += i
    return sum
