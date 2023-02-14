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

    def update(self, *args, **kwargs):
        '''Method to assigns attributes'''

        if args and len(args) != 0:
            len_args = len(args)
            att_name = ['id', 'size', 'x', 'y']
            for i in range(len_args):
                name = att_name[i]
                setattr(self, name, args[i])

        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Square'''

        new_dict = dict(
            id=self.id, size=self.size,
            x=self.x, y=self.y
        )
        return new_dict

    @property
    def size(self):
        '''Returns size'''

        return self.width

    @size.setter
    def size(self, value):
        '''Setter method for size'''

        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.width = value
        self.height = value
