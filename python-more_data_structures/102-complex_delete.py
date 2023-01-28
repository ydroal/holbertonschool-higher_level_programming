#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys = [k for k, v in a_dictionary.items() if v == value]
        if keys:
            for k in keys:
                del a_dictionary[k]
    return a_dictionary
