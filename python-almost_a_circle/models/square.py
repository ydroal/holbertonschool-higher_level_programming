#!/usr/bin/python3
'''Module to define a class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Define a Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Over writted method that return a string to print the Square.'''

        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}')
