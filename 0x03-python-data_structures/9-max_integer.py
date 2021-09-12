#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None

    current_max = my_list[0]
    for each in my_list:
        if each < current_max:
            continue
        else:
            current_max = each
    return (current_max)
