#!/usr/bin/python3
'''Unittest for max_integer([..])'''

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''test class of max_integer'''

    def test_def(self):
        '''test: normal case'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
        '''test: with negative integer'''
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_str(self):
        '''test: with string'''
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3, '4'])

    def test_strings(self):
        '''test: with strings'''

        s = 'HelloWorld'
        self.assertEqual(max_integer(s), 'r')

    def test_noargs(self):
        '''test: without args'''
        self.assertEqual(max_integer(), None)

    def test_float(self):
        '''test: with float'''
        self.assertEqual(max_integer([1.2, 2.5, 3, 4.41]), 4.41)

    def test_max_in_the_middle(self):
        '''test: max_in_the_middle'''
        self.assertEqual(max_integer([12, 51, 33]), 51)

    def test_one_element(self):
        '''test: with float'''
        self.assertEqual(max_integer([77]), 77)


if __name__ == '__main__':
    unittest.main()
