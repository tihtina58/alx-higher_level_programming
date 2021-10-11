#!/usr/bin/python3
"""Module for class that inherits from list class"""


class MyList(list):
    """class that inherits from list class"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        list_cpy = self.copy()
        list_cpy.sort()
        print(list_cpy)
