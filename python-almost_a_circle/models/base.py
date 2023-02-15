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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Method that writes the JSON string representation
        of list_objs to a file
        '''

        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        file_name = class_name + '.json'

        # Convert list_objs to list of dictionaries
        dict_list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())

        # Convert list of dictionaries to JSON string
        json_string = cls.to_json_string(dict_list)

        with open(file_name, 'w') as json_file:
            json_file.write(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method that returns the JSON string representation of list'''

        if not list_dictionaries:
            res = '[]'
        else:
            res = json.dumps(list_dictionaries)

        return res
