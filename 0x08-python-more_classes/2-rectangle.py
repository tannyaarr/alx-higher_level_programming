#!/usr/bin/python3
"""Defines the class Rectangle based on 1-rectangle.py"""


class Rectangle:

    """This class represents A Rectangle"""

    def __init__(self, width=0, height=0):
        """initializes a new Rectangle"""
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """sets the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
         self._width = value

    @property
    def height(self):
        """sets the height of the Rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area of the Rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return 2 * (self._width + self._height)
