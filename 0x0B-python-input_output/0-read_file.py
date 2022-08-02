#!/usr/bin/python3
""" func that reads a text file"""

def read_file(filename=""):
    """reads a utf8 file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
