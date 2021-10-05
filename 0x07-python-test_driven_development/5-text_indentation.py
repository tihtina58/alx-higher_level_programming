#!/usr/bin/python3
"""text_indentation function module"""


def text_indentation(text):
    """This function prints a text with 2 new
     lines after each of these characters: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")

    last_printed = '\n'
    print_space = 0

    for char in text:
        if print_space > 0 and char != '\n' and char != ' ':
            for i in range(print_space):
                print(" ", end="")
            last_printed = " "
            print_space = 0
        if char != ' ':
            if char == '\n':
                print_space = 0
            print("{}".format(char), end="")
            last_printed = char
        elif last_printed != '\n':
            print_space += 1
        if char in ".?:":
            print()
            print()
            last_printed = '\n'
