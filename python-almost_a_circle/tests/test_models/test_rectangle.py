#!/usr/bin/python3
'''Unit test for Base class'''

import unittest
import sys
from io import StringIO
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
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_width(self):
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

        with self.assertRaises(TypeError) as context:
            r = Rectangle('Hello', 30)
        self.assertEqual(str(context.exception), 'width must be an integer')

        with self.assertRaises(ValueError) as context:
            r = Rectangle(-10, 30)
        self.assertEqual(str(context.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 2)
        self.assertEqual(str(context.exception), 'width must be > 0')

    def test_height(self):
        r = Rectangle(10, 20)
        r.height = 30
        self.assertEqual(r.height, 30)

        with self.assertRaises(TypeError) as context:
            r = Rectangle(30, 'Hello')
        self.assertEqual(str(context.exception), 'height must be an integer')

        with self.assertRaises(ValueError) as context:
            r = Rectangle(30, -10)
        self.assertEqual(str(context.exception), 'height must be > 0')

        with self.assertRaises(ValueError) as context:
            r = Rectangle(1, 0)
        self.assertEqual(str(context.exception), 'height must be > 0')

    def test_x(self):
        r = Rectangle(10, 20)
        r.x = 30
        self.assertEqual(r.x, 30)

        with self.assertRaises(TypeError) as context:
            r = Rectangle(1, 2, '3')
        self.assertEqual(str(context.exception), 'x must be an integer')

        with self.assertRaises(TypeError) as context:
            r.x = 'Hello'
        self.assertEqual(str(context.exception), 'x must be an integer')

        with self.assertRaises(ValueError) as context:
            r = Rectangle(1, 2, -3)
        self.assertEqual(str(context.exception), 'x must be >= 0')

        with self.assertRaises(ValueError) as context:
            r.x = -10
        self.assertEqual(str(context.exception), 'x must be >= 0')

    def test_y(self):
        r = Rectangle(10, 20)
        r.y = 30
        self.assertEqual(r.y, 30)

        with self.assertRaises(TypeError) as context:
            r = Rectangle(1, 2, 3, '4')
        self.assertEqual(str(context.exception), 'y must be an integer')

        with self.assertRaises(TypeError) as context:
            r.y = 'Hello'
        self.assertEqual(str(context.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as context:
            r = Rectangle(1, 2, 3, -4)
        self.assertEqual(str(context.exception), 'y must be >= 0')

        with self.assertRaises(ValueError) as context:
            r.y = -10
        self.assertEqual(str(context.exception), 'y must be >= 0')

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

        with self.assertRaises(TypeError):
            r = Rectangle(3)

        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

        with self.assertRaises(TypeError):
            r = Rectangle('Hello', 2)

    def test_display(self):
        r = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        with StringIO() as output:
            sys.stdout = output
            r.display()
            self.assertEqual(output.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        expected_str = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(r), expected_str)

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 10/10')

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (89) 4/5 - 2/3')

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        r_dictionary = r.to_dictionary()
        self.assertEqual(
            r_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})


if __name__ == '__main__':
    unittest.main()
