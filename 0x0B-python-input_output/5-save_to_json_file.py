#!/usr/bin/python3
""" write an object to atext file in json"""


import json


def save_to_json_file(my_obj, filename):
    """ take object and save to file as json
    Args:
        my_obj: the object to save
        filename: file to save the obj at
    Returns:
        number of chars saved on file
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
