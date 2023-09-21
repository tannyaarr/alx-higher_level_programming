#!/usr/bin/python3
"""Defines unittests for base.py

Unittest classes:
    TestBase_constructor
    TestBase_to_json_string
    TestBase_save_to_file
    TestBase_from_json_string
    TestBase_create
    TestBase_load_from_file
    """

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty_list(self):
        result = Base.tojson_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_with_data(self):
        data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        expected_result = '[{"name": "John", "age": 30} {"name": "Jane", "age": 25}]'
        result = Base.to_json_string(data)
        self.assertEqual(result, expected_result)

    def tearDown(self):
        for cls in [Rectangle, Square]:
            filename = cls.__name__ + ".json"
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 5)
        r2 = Rectangle(7, 3)
        Rectangle.save_to_file([r1, r2])
        self.asserTrue(os.path.exits("Rectangle.json"))

    def test_save_to_file_square(self):
        s1 = Square(5)
        s2 = Square(7)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_from_json_string_empty_list(self):
        result = Base.from_json_string([])
        self.assertEqual(result, "[]")

    def test_from_json_string_none_list(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, "[]")

    def test_from_json_string_valid_json_list(self):
        input_list = [{"key1": "value1"}, {"key2": "value2"}]
        result = Base.to_json_string(input_list)
        expected = '[{"key1": "value1"}, {"key2": "value2"}]'
        self.assertEqual(result, expected)

    def test_create_rectangle(self):
        data = {'width': 5, 'height': 10, 'id': 1}
        instance = Rectangle.create(**data)
        self.assertEqual(instance.width, 5)
        self.assertEqual(instance.height, 10)
        self.assertEqual(instance.id, 1)

    def test_create_square(self):
        data = {'size': 5, 'id': 1}
        instance = Square.create(**data)
        self.assertEqual(instance.size, 5)
        self.assertEqual(instance.id, 1)

    def test_create_unsupported_class(self):
        data = {'size': 5, 'id': 1}
        with self.assertRaises(ValueError):
            instance = Base.create(**data)

    def test_load_from_file_empty(self):
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_nonexistent(self):
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_with_data(self):
        data = [{"id": 1, "width": 5, "height": 10}, {"id": 2, "size": 7}]
        filename_rect = Rectangle.__name__ + ".json"
        filename_square = Square.__name__ + ".json"
        with open(filename_rect, mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(data))
        with open(filename_square, mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(data))

        result_rect = Rectangle.load_from_file()
        result_square = Square.load_from_file()

        self.assertEqual(len(result_rect), 2)
        self.assertEqual(len(result_square), 2)


if __name__ == '__main__':
    unittest.main()

