#!/usr/bin/python3
'''Module to define a MyList'''


class MyList(list):
    '''Define a MyList.'''

    def print_sorted(self):
        '''Method that prints the list, but sorted (ascending sort)'''

        print(sorted(self))
