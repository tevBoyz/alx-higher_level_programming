#!/usr/bin/python3
""" class checking function"""


def is_same_class(obj, a_class):
    """Check if object is instance of a class

    Args:
        obj: object
        a_class: class

    Return:
        true or false
    """
    if type(obj) == a_class:
        return True
    return False
