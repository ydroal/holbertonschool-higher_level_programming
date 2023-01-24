#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_list = []
    for lst in matrix:
        new_list = list(map(lambda i: i**2, lst))
        new_matrix.append(new_list)
    return new_matrix
