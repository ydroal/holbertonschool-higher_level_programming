#!/usr/bin/python3
'''Module to print a square'''


def print_square(size):
    '''
    Print a square.

    Args:
        size (int): size length of the square

    Raises:
        TypeError: If size is not int or
                   If size is float and is less than 0.
        ValueError: If size is less than 0.

    Returns:
        Nothing
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size, end='')
        print()
