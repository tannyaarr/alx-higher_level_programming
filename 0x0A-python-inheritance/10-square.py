#!/usr/bin/python3
"""Defines the class BasedGeometry based on 6-base_geometry.py"""


class BaseGeometry:

    """This class represents a BaseGeometry"""

    def area(self):

        """ Raises an exception when area is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer is validated based on name and value or else
            rasies a TypeError or ValueError"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):

    """This class represents a Rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """Initialization of width and height takes place"""

        self.__weight = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area is calculated for width and height"""

        return self.__width * self.__height

    def __str__(self):
        """A string is returned if it id divisble"""

        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):

    """This class represents a Square based on Rectangle"""

    def __init__(self, size):
        """A super def is initilized"""

        super().__init__(size, size)

    def __str__(self):
        """A string def is declared"""

        return f"[Square] {self._Rectangle__width}"
