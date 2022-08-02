#!/usr/bin/python3
""" func that returns a dictionart desc"""


def class_to_json(obj):
    """class to json
    returns a dictionart"""
    return obj.__dict__
