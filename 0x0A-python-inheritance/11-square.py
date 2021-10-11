#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from rectangle."""
    def __init__(self, size):
        """initialize with self."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns description."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Area of square"""
        return self.__size ** 2
