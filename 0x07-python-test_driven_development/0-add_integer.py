#!/usr/bin/python3
""" Def integer addition function"""


def add_integer(a, b=98):
    """Returns the sum of a and b.

    Float args are casted to ints before operation.

    Raises:
        TypeError: if a or b is neither float nor int
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
