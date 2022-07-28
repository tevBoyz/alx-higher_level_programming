#!/usr/bin/python3
"""Module to find the max int in a list"""

def max_integer(list=[]):
    """finds a max integer in list"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            resunt = list[i]
        i += 1
    return result
