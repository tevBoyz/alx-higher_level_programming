#!/usr/bin/python3
"""
Implement geometry class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """implements rectangle"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """print"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
