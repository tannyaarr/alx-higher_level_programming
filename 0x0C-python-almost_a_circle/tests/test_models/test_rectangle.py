#!/usr/bin/python3
"""Defines all unittest for rectangle.py

Unittest classes:
    TestRectangle constructor
    TestRectangle getter_setter
    TestRectangle constructor_valid_args
    TestRectangle constructor_invalid_args
    TestRectangle setter

    """
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        r = Rectangle(10, 5, 1, 2, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.asserEqual(r.id, 100)

    def test_constructor_valid_args(self):
        r = Rectangle(10, 5, 1, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_constructor_invalid_args(self):
        with self.assertRaises(TypeError):
            r.Rectangle = ("10", 5, 1, 2)
        with self.assertRaises(ValueError):
            r.Rectangle  = (-10, 5, 1, 2)
        with self.assertRaises(TypeError):
            r.Rectangle = (10, "5", 1, 2)
        with self.assertRaises(ValueError):
            r.Rectangle  = (10, -5, 1, 2)
        with self.assertRaises(TypeError):
            r.Rectangle = (10, 5, "1", 2)
        with self.assertRaises(ValueError):
            r.Rectangle  = (10, 5, -1, 2)
        with self.assertRaises(TypeError):
            r.Rectangle = (10, 5, 1, "2")
        with self.assertRaises(ValueError):
            r.Rectangle  = (10, 5, 1, -2)


    def test_width_getter_setter(self):
        r = Rectangle(10, 5)
        r.width = 20
        self.assertEqual(r.width, 20)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.width = "string"

    def test_height_getter_setter(self):
        r = Rectangle(10, 5)
        r.height = 15
        self.assertEqual(r.height, 15)
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(TypeError):
            r.height = "string"

    def test_x_getter_setter(self):
        r = Rectangle(10, 5)
        r.x = 3
        self.assertEqual(r.x. 3)
        with self.assertRaises(ValueError):
            r.x = -1
        with self.assertRaises(TypeError):
            r.x = "string"

    def test_y_getter_setter(self):
        r = Rectangle(10, 5)
        r.y = 4
        self.asserEqual(r.y, 4)
        with self.assertRaises(ValueError):
            r.y = -2
        with self.assertRaises(TypeError):
            r.y = "string"

    def test_width_setter(self):
        r = Rectangle(10, 5, 1, 2)
        r.width = 20
        self.assertEqual(r.width, 20)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.width = "string"

    def test_height_setter(self):
        r = Rectangle(10, 5, 1, 2)
        r.height = 15
        self.assertEqual(r.height, 15)
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(TypeError):
            r.height = "string"

    def test_x_setter(self):
        r = Rectangle(10, 5, 1, 2)
        r.x = 3
        self.assertEqual(r.x, 3)
        with self.assertRaises(ValueError):
            r.x = -1
        with self.assertRaises(TypeError):
            r.x = "string"

    def test_y_setter(self):
        r = Rectangle(10, 5, 1, 2)
        r.y = 4
        self.assertEqual(r.y, 4)
        with self.assertRaises(ValueError):
            r.y = -10
        with self.assertRaises(TypeError):
            r.y = "string"


if __name__ = '__main__':
    unittest.main()
