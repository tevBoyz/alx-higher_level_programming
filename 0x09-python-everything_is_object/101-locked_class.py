#!/usr/bin/python3
""" Locked Class"""


class LockedClass:
    """
    class that prevents instances from being created
    but only for attributes called 'first_name'
    """

    __slots__ = ["first_name"]
