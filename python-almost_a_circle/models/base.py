#!/usr/bin/python3
'''Module to define a class Base'''


class Base:
    '''Define a Base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize'''

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
