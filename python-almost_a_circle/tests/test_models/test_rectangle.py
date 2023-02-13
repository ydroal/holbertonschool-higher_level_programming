#!/usr/bin/python3
'''Unit test for Base class'''

import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    '''Test class for Rectangle'''

    def test_init_with_id(self):
        r = Rectangle(10, 20, 1, 2, 123)
        self.assertEqual(r.id, 123)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_init_without_id(self):
        r = Rectangle(30, 10, 1, 2)
        self.assertIsNotNone(r.id)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)


if __name__ == '__main__':
    unittest.main()
