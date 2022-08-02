#!/usr/bin/python3
""" defines a function that adds an attribute to objects"""


def add_attribute(obj, att, value):
    """ add attribute to object if possible
    Args:
        obj: object
        att: attribute to add
        value: value of att
    Raises:
        TypeError: if attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
