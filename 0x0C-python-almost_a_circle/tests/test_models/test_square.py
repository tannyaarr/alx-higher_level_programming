#!/usr/bin/python3
"""Defines square.py inherited from rectangle.py

Unittest classes:
    TestSquare_area
    TestSquare_size
    TestSquare_args
    TestSquare_kwargs
    """
import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_attributes(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, None)

    def test_square_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 5)

    def test_square_str(self):
        s = Square(5, 1, 2, 100)
        self.assertEqual(str(s), "[Square] (100) 1/2 - 5")

    def test_square_update(self):
        s = Square(5, 1, 2, 100)
        s.update(101, 6, 3, 4)
        self.assertEqual(s.id, 101)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_size_setter(self):
        s = Square(5)
        s.size = 7
        self.assertEqual(s.size, 7)
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)

    def test_square_size_setter_invalid(self):
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -1
        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_square_update_with_args(self):
        s = Square(5, 1, 2, 100)
        s.update(101, 6, 3, 3)
        self.assertEqual(s.id, 101)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_update_with_kwargs(self):
        s = Square(5, 1, 2, 100)
        s.update(id=101, size=6, x=3, y=4)
        self.assertEqual(s.id, 101)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_update_mixed_args_kwargs(self):
        s = Square(5, 1, 2, 100)
        s.update(101, 6, x=3, y=4)
        self.assertEqual(s.id, 101)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_update_invalid_args(self):
        s = Square(5, 1, 2, 100)
        with self.assertRaises(IndexError):
            s.update()
        with self.assertRaises(IndexError):
            s.update(101, 6, 3)
        with self.assertRaises(ValueError):
            s.update(101, -1, 3, 4)

    def test_square_to_dictionary(self):
        s = Square(5, 1, 2, 100)
        dictionary = s.to_dictionary()
        self.assertEqual(dictionary. {'id': 100, 'size': 5, 'x': 1, 'y': 2 })


if __name__ == '__main__':
    unittest.main()
