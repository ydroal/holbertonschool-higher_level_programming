#!/usr/bin/python3
'''Module to define a rectangle'''


class Rectangle:
    '''Define a rectangle'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Initialize rectangle with a given size.'''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        '''Method that returns the rectangle area'''

        return self.__height * self.__width

    def perimeter(self):
        '''Method that returns the rectangle perimeter'''

        if self.__width == 0 or self.__height == 0:
            return 0

        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''Method that return a string to print a rectangle.'''

        if self.__width == 0 or self.__height == 0:
            return ''

        else:
            return '\n'.join(('#' * self.__width)
                             for _ in range(self.__height))

    def __repr__(self):
        '''
        Method that return a string representation of
        the rectangle to be able to recreate a new instance by using eval()
        '''

        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        '''
        Method thet print the message Bye rectangle...
        when an instance of Rectangle is deleted
        and decrement number_of_instances.
        '''
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
