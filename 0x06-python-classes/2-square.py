#!/usr/bin/python3
"""Square class"""


class Square:
    """square class definintion"""

    def __init__(self, size=0):
        """Constructor

        args:
            size: size of sides of square

        Raises:
            TypeError: if size is not integer
            ValueError: if size i < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
