#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    else:
        res = ''
        for c in my_string:
            if c not in 'cC':
                res += c
        return res
