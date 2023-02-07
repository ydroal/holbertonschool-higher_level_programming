#!/usr/bin/python3
'''Module to define a class BaseGeometry'''


class BaseGeometry:
    '''Define a BaseGeometry'''

    def area(self):
        '''Method that raises an Exception with the message'''

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Method that validates value
        Args:
            name: str
            value: int

        '''

        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
