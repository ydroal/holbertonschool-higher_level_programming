#!/usr/bin/python3
'''Module to define a class Student'''


class Student:
    '''Define a Student'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Method that retrieves a dictionary representation of
        a Student instance.
        -If attrs is a list of strings, only attribute names contained
         in this list must be retrieved.
        -Otherwise, all attributes must be retrieved.
        '''

        j_dic = self.__dict__
        if not attrs:
            return j_dic

        else:
            new_dic = {}
            for k in j_dic:
                if k in attrs:
                    new_dic[k] = j_dic[k]

        return new_dic
