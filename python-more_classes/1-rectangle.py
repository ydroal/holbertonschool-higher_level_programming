#!/usr/bin/python3
'''Module to define a rectangle'''


class Rectangle:
    '''Define a rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialize rectangle with a given size.'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Getter method for the value of `__width`.
        Returns:
            int: The value of __width.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for the 'width' property.'''

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Getter method for the value of `__height`.
        Returns:
            int: The value of __height.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for the 'height' property.'''

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
