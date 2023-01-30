#!/usr/bin/python3
'''Module to define a square.'''


class Square:
    '''Define a square.'''

    def __init__(self, size=0):
        '''Initialize square with a given size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        '''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
