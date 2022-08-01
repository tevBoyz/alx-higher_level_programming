#!/usr/bin/python3
""" inherits from"""


def inherits_from(obj, a_class):
    """ check inherintance of obj from a class
    Args:
        obj: object
        a_class: class
    Return: true or false
    """
    return type(obj) != a_class and isinstance(obj, a_class)
