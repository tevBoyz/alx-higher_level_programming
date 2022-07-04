#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        res = []
        for i in my_list:
            if i % 2 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
