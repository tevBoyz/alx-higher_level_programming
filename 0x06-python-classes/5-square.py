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

    def my_print(self):
        """ print area to stdout using #"""
        if self.__size == 0:
            print()
        else:
            w = self.__size
            h = self.__size
            while h > 0:
                for i in range(0, w):
                    print("#", end='')
                print()
                h -= 1

