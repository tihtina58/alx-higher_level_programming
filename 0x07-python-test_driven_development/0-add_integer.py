#!/usr/bin/python3
"""Here you will find a function that adds two integers."""


def add_integer(a, b=98):
    """Function that takes 2 integers and
       returns their sum"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
