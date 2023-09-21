#!/usr/bin/python3
"""Defines all unittest for rectangle.py

Unittest classes:
    TestRectangle_constructor
    TestRectangle_getter_setter
    TestRectangle_constructor_valid_args
    TestRectangle_constructor_invalid_args
    TestRectangle_setter
    TestRectangle_args
    TestRectangle_kwargs

    """
import unittest
import sys
from models.rectangle import Rectangle
from io import StringIO

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

    def test_display(self):
        r = Rectangle(3, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = "###\n###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(3, 2, 1, 2, 100)
        expected_str = "[Rectangle] (100) 1/2 - 3/2"
        self.assertEqual(str(r), expected_str)

    def test_upadted_display(self):
        r = Rectangle(3, 2, 1, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n\n ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update(self):
        r = Rectangle(1, 1)
        r.update(100)
        self.assertEqual(r.id, 100)
        r.update(100, 10)
        aelf.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        r.update(100, 10, 20)
        self.assertEqual(r.id, 100)
        self.asserrEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        r.update(100, 10, 20, 30)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        r.update(100, 10, 20, 30, 40)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)

     def test_update_with_args(self):
        r = Rectangle(1, 1)
        r.update(100)
        self.assertEqual(r.id, 100)
        r.update(100, 10)
        aelf.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        r.update(100, 10, 20)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        r.update(100, 10, 20, 30)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        r.update(100, 10, 20, 30, 40)
        self.asserEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)

     def test_update_with_kwargs(self):
        r = Rectangle(1, 1)
        r.update(id=100)
        self.assertEqual(r.id, 100))
        r.update(id=100, width=10)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        r.update(id=100, width=10, height=20)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        r.update(id=100, width=10, height=20, x=30)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        r.update(id=100, width=10, height=20, x=30, y=40)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)

    def test_rectangle_to_dictionary(self):
        r = Rectangle(5, 4, 1, 2, 100)
        dictionary = r.to_dictionary()
        self.assertEqual(dictionary. {'id': 100, 'width': 5, 'height': 4 'x': 1, 'y': 2 })

if __name__ = '__main__':
    unittest.main()
