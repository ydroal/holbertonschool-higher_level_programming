#!/usr/bin/python3
'''Module to define a function save_to_json_file'''

import json


def save_to_json_file(my_obj, filename):
    '''
    Function that writes an Object to a text file,
    using a JSON representation
    '''

    with open(filename, 'w') as f:
        json.dump(my_obj, f)

    return filename
