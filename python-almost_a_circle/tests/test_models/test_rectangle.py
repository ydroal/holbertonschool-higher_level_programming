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


if __name__ == '__main__':
    unittest.main()
