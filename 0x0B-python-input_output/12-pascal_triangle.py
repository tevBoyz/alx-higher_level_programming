#!/usr/bin/python3
""" Pascal's triangle"""


def pascal_triangle(n):
    """ represnt pascal triangle of size n
    Return: a list of lists"""

    if n <= 0:
        return []

    tris = [[1]]
    while len(tris) != n:
        tri = tris[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        tris.append(temp)
    return tris
