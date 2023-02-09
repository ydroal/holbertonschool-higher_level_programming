#!/usr/bin/python3
'''Module to define a function load_from_json_file'''

import json


def load_from_json_file(filename):
    '''Function that creates an Object from a “JSON file”'''

    with open(filename) as f:
        res = json.load(f)

    return res
