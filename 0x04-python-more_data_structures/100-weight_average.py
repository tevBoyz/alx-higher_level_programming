#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    return sum([x[0] * x[1] for x in my_list]) / \
            (sum([x[1] for x in my_list] or 1))
