#!/usr/bin/python3
""" defines a geometry class """


class BaseGeometry:
    """ Class: BaseGeometry"""

    def area(self):
        """ not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate a parameter as integer
        Args:
            name: name of parameter
            value: param to validate
        Raises:
            TypeError: if val is not an integer
            ValueError: if value is <=0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
