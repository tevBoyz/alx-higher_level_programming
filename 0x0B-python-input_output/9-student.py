#!/usr/bin/python3
""" class student"""


class Student:
    """module class student"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ convert to json"""
        return self.__dict__
