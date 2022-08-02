#!/usr/bin/python3
""" Define class MyInt inherinting from int """


class MyInt(int):
    """inverts == and != operations"""
    def __eq__(self, value):
        """ override  == """
        return self.real != value

    def __ne__(self, value):
        """ override != """
        return self.real == value
