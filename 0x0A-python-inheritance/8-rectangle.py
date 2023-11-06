#!/usr/bin/python3
"""Defines the class BasedGeometry based on 7-base_geometry.py"""


class BaseGeometry:

    """This class represents a BaseGeometry"""

    def area(self):

        """ Raises an exception when area is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating the value, assuming the name is always a string"""

        """Raises TypeError if value is not an in and ValueError
            if value is less or equal to 0"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):

    """This class represents a Rectangle inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Initialization of width and height"""

        self.__weight = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
