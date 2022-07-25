#!/usr/bin/python3
"""
Rectangle module definition
"""


class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        constructor
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            value(int): width of rect
        raises:
            Type and Value error
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            value (int): new height
        raises:
            Type od value errro
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """return string representation of the rectangle"""
        ret = ""
        if self.__width == 0 or self.__height == 0:
            return ("")

        for idx in range(self.__height):
            ret += str(self.print_symbol) * self.width
            if idx + 1 < self.__height:
                ret += '\n'
        return ret

    def __repr__(self):
        """return string rep"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """delete instance of rectangle class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ return rect with bigger area
        Args:
            rect_1 (Rectangle): Rectangle object
            rect_2 (Rectangle): Rectangle object
        Raises:
            Type error
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        class method that creates a square which is type is rectangle
        """
        return cls(size, size)
