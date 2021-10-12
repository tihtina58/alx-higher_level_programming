#!/usr/bin/python3
"""Module of write_file function."""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    (UTF8) and returns the number of characters written"""
    num_chr = 0
    with open(filename, mode='w', encoding='utf-8') as myfile:
        num_chr = myfile.write(text)
    return num_chr
