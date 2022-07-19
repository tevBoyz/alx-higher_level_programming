#!/usr/bin/python3
""" Magic class """

import math


class MagicClass:
    """define a circle"""

    def __init__(self, radius=0):
        """constructor
        Args:
            radius (float or int): radius of circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """get area of a circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """get circumference of circle"""
        return (2 * math.pi * self.__radius)
