#!/usr/bin/python3
'''Unit test for Square class'''

import unittest
from models.square import Square


class Test_Square(unittest.TestCase):
    '''Test class for Square'''

    def test_init_with_id(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (4) 2/3 - 1')

    def test_init_without_id(self):
        s = Square(5)
        self.assertIsNotNone(s.id)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s1 = Square(2, 2)
        self.assertIsNotNone(s1.id)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)

        with self.assertRaises(ValueError) as e:
            s2 = Square(0)
        self.assertEqual(str(e.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as e:
            s3 = Square(-1)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_x(self):
        s = Square(10)
        s.x = 20
        self.assertEqual(s.x, 20)

        with self.assertRaises(ValueError) as context:
            s1 = Square(1, -2)
        self.assertEqual(str(context.exception), 'x must be >= 0')

        with self.assertRaises(TypeError) as context:
            s2 = Square(1, 'Hello')
        self.assertEqual(str(context.exception), 'x must be an integer')

    def test_y(self):
        s = Square(10, 20)
        s.y = 30
        self.assertEqual(s.y, 30)

        with self.assertRaises(TypeError) as context:
            s1 = Square(1, 2, '3')
        self.assertEqual(str(context.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as context:
            s2 = Square(1, 2, -3)
        self.assertEqual(str(context.exception), 'y must be >= 0')

    def test_update(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(str(s), '[Square] (89) 10/10 - 10')

        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (1) 3/4 - 2')

        s.update(x=1)
        self.assertEqual(str(s), '[Square] (1) 1/4 - 2')

        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), '[Square] (89) 1/1 - 7')


if __name__ == '__main__':
    unittest.main()
