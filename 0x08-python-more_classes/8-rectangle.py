#!/usr/bin/python3
"""Module defining the Rectangle class"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle based on its height and width
    area and perimeter methodes included
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize rectangle with private width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def area(self):
        """"instance method that returns the area"""
        return self.width * self.height

    def perimeter(self):
        """instance method that returns the rectangle's perimeter"""
        if self.width == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """returns a string that can be printed like a rectangle"""
        rect = ""
        for i in range(self.height):
            for j in range(self.width):
                rect += str(self.print_symbol)
            if i != self.height - 1 and self.width != 0:
                rect += '\n'
        return rect

    def __repr__(self):
        """returns the a representation of the self object"""
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """It is called when the instance is about to be destroyed"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @property
    def height(self):
        """getter for height attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
