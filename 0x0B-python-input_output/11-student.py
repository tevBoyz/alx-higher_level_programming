#!/usr/bin/python3
""" class student"""


class Student:
    """module class student"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ convert to json
        Args:
            attrs: attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attr of student
        Args:
            json: key/val pairs to replace with
        """
        for k, v in json.items():
            setattr(self, k, v)
