#!/usr/bin/python3
'''Module to divid all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''
    Divid all elements of a matrix.
    Args:
        matrix (list): list of lists of integers or floats.
        div (int or float): A number to divide.
    Raises:
        TypeError: If matrix is not a list of lists of int or float.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is equal to 0.
    Returns:
        list: A new matrix with result of calculation.
    '''

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or (len(matrix) == 0) or \
       type(matrix[0]) is not list or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for c in row:
            if type(c) is not int and type(c) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    return [[round(item / div, 2) for item in row] for row in matrix]
