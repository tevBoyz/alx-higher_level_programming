#!/usr/bin/python3
""" outputs a string to textfile"""


def write_file(filename="", text=""):
    """module to write to file"""
    with open(filename, "w") as f:
        return f.write(text)
