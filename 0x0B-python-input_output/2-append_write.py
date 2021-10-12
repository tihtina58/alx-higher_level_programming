#!/usr/bin/python3
"""Module of write_file function."""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added"""
    num_chr = 0
    with open(filename, mode='a', encoding='utf-8') as myfile:
        num_chr = myfile.write(text)
    return num_chr
