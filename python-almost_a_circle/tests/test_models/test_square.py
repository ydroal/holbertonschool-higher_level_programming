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

        with self.assertRaises(TypeError) as e:
            s2 = Square('1')
        self.assertEqual(str(e.exception), 'width must be an integer')

        with self.assertRaises(ValueError) as e:
            s3 = Square(0)
        self.assertEqual(str(e.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as e:
            s4 = Square(-1)
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

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 9)
        s_dictionary = s.to_dictionary()
        self.assertEqual(
            s_dictionary, {'id': 9, 'size': 10, 'x': 2, 'y': 1})

    def test_create(self):
        s_dict = {'id': 89}
        s = Square.create(**s_dict)
        self.assertEqual(str(s), '[Square] (89) 0/0 - 10')

        s_dict1 = {'id': 89, 'size': 1}
        s1 = Square.create(**s_dict1)
        self.assertEqual(str(s1), '[Square] (89) 0/0 - 1')

        s_dict2 = {'id': 89, 'size': 1, 'x': 2}
        s2 = Square.create(**s_dict2)
        self.assertEqual(str(s2), '[Square] (89) 2/0 - 1')

        s_dict3 = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s3 = Square.create(**s_dict3)
        self.assertEqual(str(s3), '[Square] (89) 2/3 - 1')

    def test_save_to_file(self):
        s1 = Square(10, 5, 5, 1)
        Square.save_to_file([s1])
        with open('Square.json', 'r') as file:
            read = file.read()
            self.assertEqual(read, '[{"id": 1, "size": 10, "x": 5, "y": 5}]')

    def test_save_to_file_list_with_emp(self):
        Square.save_to_file([])
        with open('Square.json', 'r') as file:
            read = file.read()
            self.assertEqual(read, '[]')

    def test_save_to_file_emp2(self):
        Square.save_to_file(None)
        with open('Square.json', 'r') as file:
            read = file.read()
            self.assertEqual(read, '[]')

    def test_load_from_file(self):
        s = Square.load_from_file()
        self.assertEqual(s, [])

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        li_Squares = [s1, s2]
        Square.save_to_file(li_Squares)
        out = Square.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertEqual(type(out[0]), Square)
        self.assertEqual(type(out[1]), Square)
        self.assertEqual(s1.x, out[0].x)
        self.assertEqual(s1.y, out[0].y)
        self.assertEqual(s1.size, out[0].size)
        self.assertEqual(s2.x, out[1].x)
        self.assertEqual(s2.y, out[1].y)
        self.assertEqual(s2.size, out[1].size)


if __name__ == '__main__':
    unittest.main()
