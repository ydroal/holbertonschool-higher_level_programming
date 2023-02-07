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
