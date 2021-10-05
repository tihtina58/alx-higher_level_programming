#!/usr/bin/python3
"""Divide a matrix Module"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.
       matrix must be a matrix (list of lists) of integers/floats.
       div must be a number != 0"""
    len_rows = 0
    new_matrix = []

    if type(div) not in (float, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    try:
        len_rows = len(matrix[0])
    except:
        pass

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of"
                            " integers/floats")
        if len(row) != len_rows:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")

    for row in matrix:
        current_row = []
        for element in row:
            current_row.append(round(element / div, 2))
        new_matrix.append(current_row)
    return new_matrix
