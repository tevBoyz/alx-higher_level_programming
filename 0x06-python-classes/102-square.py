#!/usr/bin/python3
"""square class"""


class Square:
    """Square definition"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: size of sides

        Raises:
            ValueError: if size < 0
            TypeError: if size is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """property getter

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter

        args:
            value: new value

        Raises:
            ValueError: if value is < 0
            TypeError: if value is not integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of a square

        Return:
            the size squared
        """
        return self.__size ** 2

    def __eq__(self, other):
        """define == comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """ define != comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """define < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """define <= comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """define >= comparison"""
        return self.area() >= other.area()
