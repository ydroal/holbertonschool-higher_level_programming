#!/usr/bin/python3
'''Module to define a class Base'''

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method that returns the JSON string representation of list'''

        return json.dumps(list_dictionaries)
