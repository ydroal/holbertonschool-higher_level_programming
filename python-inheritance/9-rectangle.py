#!/usr/bin/python3
'''Module to define a class Rectangle'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Define a Rectangle'''

    def __init__(self, width, height):
        '''Initialize rectangle'''

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method that return area of square'''

        return self.__width * self.__height

    def __str__(self):
        '''Method that return a string to print a rectangle description'''

        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
