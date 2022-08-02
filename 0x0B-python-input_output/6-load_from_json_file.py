#!/usr/bin/python3
"""function reading from json file"""


import json


def load_from_json_file(filename):
    """make object from json file"""
    with open(filename) as f:
        return json.load(f)
