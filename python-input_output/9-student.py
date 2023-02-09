#!/usr/bin/python3
'''Module to define a class Student'''


class Student:
    '''Define a Student'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        Method that retrieves a dictionary representation of
        a Student instance'''

        return self.__dict__
