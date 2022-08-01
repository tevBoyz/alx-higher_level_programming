#!/usr/bin/python3
""" class inherits from list"""


class MyList(list):
    """module mylist"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
