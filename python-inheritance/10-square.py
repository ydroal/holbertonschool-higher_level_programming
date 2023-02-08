#!/usr/bin/python3
'''Module to define a class Square'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Define a Square'''

    def __init__(self, size):
        '''Initialize Square'''

        super(Rectangle, self).integer_validator('size', size)
        self.__size = size

    def area(self):
        '''Overriding method that return area of square'''

        return self.__size**2

    def __str__(self):
        '''Overriding method that return a string to print'''

        return ('[Rectangle] {}/{}'.format(self.__size, self.__size))
