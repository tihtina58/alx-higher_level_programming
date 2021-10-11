#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class."""
    def area(self):
        """raise a exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value. It has to be an
        integer greater than zero."""
        if type(value) != int:
            raise Exception("{} must be an integer".format(name))
        elif value <= 0:
            raise Exception("{} must be greater than 0".format(name))
