#!/usr/bin/python3
'''Module to define a class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Define a BaseGeometry'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Returns width'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for width'''

        self.__width = value

    @property
    def height(self):
        '''Returns height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for height'''

        self.__height = value

    @property
    def x(self):
        '''Returns x'''

        return self.__x

    @x.setter
    def x(self, value):
        '''Setter method for x'''

        self.__x = value

    @property
    def y(self):
        '''Returns y'''

        return self.__y

    @y.setter
    def y(self, value):
        '''Setter method for y'''

        self.__y = value
