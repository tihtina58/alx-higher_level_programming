#!/usr/bin/python3
"""print_square function module"""


def print_square(size):
    """function that prints a square with the character #.
    size is the size length of the square"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for colum in range(size):
            print("#", end="")
        print()
