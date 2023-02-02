#!/usr/bin/python3
'''Module to prints My name'''


def say_my_name(first_name, last_name=""):
    '''
    Print a name.

    Args:
        first_name (string): list of lists of integers or floats.
        last_name (string): A number to divide.

    Raises:
        TypeError: If two of args are not a strings.

    Returns:
        Nothing
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {:s} {:s}'.format(first_name, last_name))
