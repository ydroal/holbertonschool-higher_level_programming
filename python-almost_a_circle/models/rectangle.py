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

    def area(self):
        '''Method that returns the area value of the Rectangle instance.'''

        return self.__width * self.__height

    @property
    def width(self):
        '''Returns width'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for width'''

        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        '''Returns height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for height'''

        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        '''Returns x'''

        return self.__x

    @x.setter
    def x(self, value):
        '''Setter method for x'''

        if type(value) is not int:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        '''Returns y'''

        return self.__y

    @y.setter
    def y(self, value):
        '''Setter method for y'''

        if type(value) is not int:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value
