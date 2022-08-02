#!/usr/bin/python3
""" a function to append to file"""


def append_write(filename="", text=""):
    """append a string to text file
    Args:
        filename: name of the text file
        text: string to append
    Return:
        The number of chars appened
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
