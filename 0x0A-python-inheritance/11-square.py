#!/usr/bin/python3
""" more"""


Rectangle = __import__('9-rectangle').Rectangle


"""Square class"""


class Square(Rectangle):
    """Squre class"""
    def __init__(self, size):
        """constructor"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[square] " + str(self.__size) + "/" + str(self.__size))
