#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_attributes(self):
        s = Square(5, 2, 1, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 1)

    def test_square_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_str(self):
        s = Square(5, 2, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 2/3 - 5")

    def test_square_update(self):
        s = Square(5)
        s.update(10, 7, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)


    def test_square_to_dictionary(self):
        s = Square(5, 1, 2, 100)
        dictionary = s.to_dictionary()
        self.assertEqual(dictionary, {'id': 100, 'size': 5, 'x': 1, 'y': 2 })

if __name__ == '__main__':
    unittest.main()
