#!/usr/bin/python3
"""square class"""


class Square:
    """Square definition"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor

        Args:
            size(int): size of sides
            position(in tuples): position of the square

        Raises:
            ValueError: if size < 0
            TypeError: if size is not an integer
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property size getter

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

    @property
    def position(self):
        """property position getter

        Return: position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """property setter for position

        args:
            value: new position

        Raises:
            TypeError: if new value is not tuple of positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
