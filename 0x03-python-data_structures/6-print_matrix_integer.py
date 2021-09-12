#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        length = len(matrix[i]) - 1
        for x in range(len(matrix[i])):
            print("{:d}".format(matrix[i][x]), end="")
            if x != length:
                print(" ", end="")
        print("")
