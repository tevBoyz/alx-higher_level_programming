#!/usr/bin/python3
"""more class base"""


Rectangle = __import__('9-rectangle').Rectangle

"""Square class"""


class Square(Rectangle):
    """Square module"""
    def __init__(self, size):
        """constructor"""
        self.__size = size
        super().__init__(self.__size, self.__size)
