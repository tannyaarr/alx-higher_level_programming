#!/usr/bin/python3
"""Defines the class Rectangle based on 0-rectangle.py"""


class Rectangle:

    """This class represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Sets the width of the rectangle"""
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
        """set the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
