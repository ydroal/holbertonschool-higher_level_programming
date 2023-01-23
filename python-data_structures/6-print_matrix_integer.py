#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for i in range(len(list)):
            idx = i
            element = list[i]
            if idx != len(list) - 1:
                print('{:d}'.format(element), end=' ')
            else:
                print('{:d}'.format(element))
