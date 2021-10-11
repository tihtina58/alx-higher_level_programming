#!/usr/bin/python3
"""Module for MyInt."""


def MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, other):
        """Are myint object and other object differents?"""
        return self != other

    def __ne__(self, other):
        """Are myint object and other object equalss?"""
        return self == other
