#!/usr/bin/python3
"""from json to object of py structure"""


import json


def from_json_string(my_str):
    """json to string"""
    return json.loads(my_str)
