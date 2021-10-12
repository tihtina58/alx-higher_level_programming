#!/usr/bin/python3
"""Module for number_of_lines function."""


def number_of_lines(filename=""):
    """function that returns the number
    of lines of a text file"""
    with open(filename, encoding='utf-8') as myfile:
        num_lines = 0
        while True:
            line = myfile.readline()
            if line == "":
                break
            num_lines += 1

    return num_lines
