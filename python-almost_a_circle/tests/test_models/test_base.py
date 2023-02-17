#!/usr/bin/python3
'''Unit test for Base class'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

        dictionary2 = Base.to_json_string([])
        self.assertEqual(dictionary2, '[]')

        dictionary3 = Base.to_json_string(None)
        self.assertEqual(dictionary3, '[]')


if __name__ == '__main__':
    unittest.main()
