#!/usr/bin/python3
'''Module to define a square.'''


class Square:
    '''Define a square.'''

    def __init__(self, size=0):
        '''
        Initialize square with a given size.

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

    def area(self):
        '''
        Instance method for calculate the current square area.

        Returns:
            int: the current square area.
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''
        Getter method for the value of the private attribute `__size`.

        Returns:
            int: The size of the object.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter method for the private attribute `__size`.
        It sets the size to the given value if it is an integer >= 0.

        Args:
            value (int): the new size to set

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
