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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if isinstance(position, tuple) and len(position) == 2:
            if isinstance(position[0], int) and isinstance(position[1], int):
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            i, j = 0, 0
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * self.__position[0],
                                    "#" * self.__size))
