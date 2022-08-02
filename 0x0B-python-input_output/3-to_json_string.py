#!/usr/bin/python3
""" object to json function """


import json


def to_json_string(my_obj):
    """returns a json represntaion of an object
    Args:
        my_obj: object to represent
    Return:
        json representation of the object
    """
    return json.dumps(my_obj)
