#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    top = 0
    bot = 0

    for i, j in my_list:
        top += i * j
        bot += j

    return top / bot
