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

    @classmethod
    def create(cls, **dictionary):
        '''Method hat returns an instance with all attributes already set'''

        class_name = cls.__name__

        if class_name == 'Rectangle':
            new_class = cls(10, 20)

        elif class_name == 'Square':
            new_class = cls(10)

        new_class.update(**dictionary)
        return new_class

    @classmethod
    def load_from_file(cls):
        '''Method that returns a list of instances'''

        class_name = cls.__name__
        file_name = class_name + '.json'

        # Read JSON string
        try:
            with open(file_name) as json_file:
                json_string = json_file.read()
        except FileNotFoundError:
            return []

        # Convert JSON string to list of dictionaries
        dic = cls.from_json_string(json_string)

        # Create instances
        list_instances = []
        for d in dic:
            instance = cls.create(**d)
            list_instances.append(instance)

        return list_instances

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method that returns the JSON string representation of list'''

        if not list_dictionaries:
            res = '[]'
        else:
            res = json.dumps(list_dictionaries)

        return res

    @staticmethod
    def from_json_string(json_string):
        '''
        Method that returns the list of the JSON string representation
        of list(json_string)
        '''

        if not json_string:
            res = []
        else:
            res = json.loads(json_string)

        return res
