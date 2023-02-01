#!/usr/bin/python3
'''Module to add two integers'''


def add_integer(a, b=98):
    '''
    Adds two integers and returns the result of culculation (int).

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer or a float.

    Returns:
        int: The sum of 'a' and 'b', casted to an integer\
             if either of them is a float.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
