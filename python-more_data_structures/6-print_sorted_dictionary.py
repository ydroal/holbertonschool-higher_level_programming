#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    new_order = sorted(a_dictionary.keys())
    for key in new_order:
        print('{:s}: {}'.format(key, a_dictionary[key]))
