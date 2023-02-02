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
    if not isinstance(matrix, list) or \
            not all(isinstance(el, list) for el in matrix):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if not all(isinstance(el, (int, float)) for li in matrix for el in li):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    length = [len(matrix[i]) for i in range(len(matrix))]
    if not all(val == length[0] for val in length):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]
    return new_matrix
