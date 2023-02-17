#!/usr/bin/python3
'''Unit test for Base class'''

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    '''Test class for Base'''

    def test_id(self):
        # Create two Base instances
        base1 = Base()
        base2 = Base()

        # IDs are unique
        self.assertNotEqual(base1.id, base2.id)

        # ID can be assigned
        base3 = Base(100)
        self.assertEqual(base3.id, 100)

        # ID can be zero
        base4 = Base(0)
        self.assertEqual(base4.id, 0)

        # ID can be negative
        base5 = Base(-1)
        self.assertEqual(base5.id, -1)

        base6 = Base()
        self.assertEqual(base6.id, 3)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_str = Base.to_json_string([dictionary])
        self.assertEqual(type(json_str), str)

        json_str2 = Base.to_json_string([])
        self.assertEqual(json_str2, '[]')

        json_str3 = Base.to_json_string(None)
        self.assertEqual(json_str3, '[]')

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_save_to_file(self):
        r1 = Rectangle(10, 20, 1, 2, 123)
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as file:
            read = file.read()
        self.assertEqual(read, '[]')

        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as file:
            read = file.read()
        self.assertEqual(read, '[]')

        Rectangle.save_to_file([r1])
        with open('Rectangle.json', 'r') as file:
            read = file.read()
            expected_op = ('[{"id": 123, "width": 10, "height": 20,'
                           ' "x": 1, "y": 2}]')
            self.assertEqual(read, expected_op)


if __name__ == '__main__':
    unittest.main()
