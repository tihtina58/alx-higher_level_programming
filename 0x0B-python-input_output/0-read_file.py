#!/usr/bin/python3
"""Module of read_file function."""


def read_file(filename=""):
    """Function that reads a text file (UTF8)
    and prints it to stdout:"""
    with open(filename, encoding='utf-8') as myfile:
        while True:
            line = myfile.readline()
            if line == "":
                break
            print("{}".format(line), end='')
