#!/usr/bin/python3
"""Module for function lookup"""


def lookup(obj):
    """function that returns the list of available
    attributes and methods of an object"""
    return dir(obj)
