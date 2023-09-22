#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0 # Reseting the counter before each test

    def test_base_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_custom_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_base_multiple_custom_ids(self):
        b1 = Base(5)
        b2 = Base(20)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 20)

    def test_base_negative_custom_id(self):
        b = Base(-100)
        self.assertEqual(b.id, -100)

    def test_base_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")
    
    def test_base_to_json_string_non_empty_list(self):
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_str = Base.to_json_string(data)
        expected_json = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(json_str, expected_json)

if __name__ == '__main__':
    unittest.main()
