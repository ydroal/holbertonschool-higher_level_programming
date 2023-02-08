#!/usr/bin/python3
'''Module to define a function read_file'''


def read_file(filename=""):
    '''function that reads a text file (UTF8) and prints it to stdout'''

    with open(filename, encoding='utf-8') as f:
        s = f.read()
        print(s, end='')
