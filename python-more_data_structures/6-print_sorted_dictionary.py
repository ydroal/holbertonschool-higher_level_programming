#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.items())
    new_dict = dict((x, y) for x, y in new_dict)

    for x, y in new_dict.items():
        print('{:s}: {}'.format(x, y))
