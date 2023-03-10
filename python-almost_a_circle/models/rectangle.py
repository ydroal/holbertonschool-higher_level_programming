#!/usr/bin/python3
'''Module to define a class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Define a Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''Method that return a string to print the Rectangle instance.'''

        return (f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}')

    def area(self):
        '''Method that returns the area value of the Rectangle instance.'''

        return self.__width * self.__height

    def display(self):
        '''Method that prints in stdout the Rectangle with the character #'''

        print('\n' * self.__y, end='')
        print('\n'.join((' ' * self.__x + '#' * self.__width)
              for _ in range(self.__height)))

    def update(self, *args, **kwargs):
        '''Method that assigns an argument to each attribute.'''

        if args and len(args) != 0:
            len_args = len(args)
            att_name = ['id', 'width', 'height', 'x', 'y']
            for i in range(len_args):
                name = att_name[i]
                setattr(self, name, args[i])

        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Rectangle'''

        new_dict = dict(
            id=self.id, width=self.width,
            height=self.height, x=self.x, y=self.y
        )
        return new_dict

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
