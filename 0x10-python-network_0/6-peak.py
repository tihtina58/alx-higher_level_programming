#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """find the peak in the list."""
    length = len(list_of_integers)
    if length == 0:
        return None

    list_of_integers.sort()

    return list_of_integers[-1]
