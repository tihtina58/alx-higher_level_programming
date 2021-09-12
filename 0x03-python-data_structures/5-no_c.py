#!/usr/bin/env python3
def no_c(my_string):
    length = len(my_string)
    for i in range my_string:
        if my_string[i] == 'C' or my_string[i] == 'c':
            my_string[i] = []
    return(my_string)
