#!/usr/bin/python3
""" square defn"""


class Square:
    """ square definition"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor

        Args:
            size(int): size of square side
            position: position of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter a new val to a  proprty
        Args:
            value: new value
        Raises:
            TypeError: if val is not an int
            ValueError: if val < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter fo current position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print the area of a square"""
        if (self.__size == 0):
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__position):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """print the representation of square"""
        if (self.__size != 0):
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return("")
