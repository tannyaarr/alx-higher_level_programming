#!/usr/bin/python3
"""Defines the class Rectangle by 8-rectangle.py"""


class Rectangle:
    """This represents the class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    """Initializes the width and height of the rectangle"""

    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    """calculates area and perimeter of the rectangle"""

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    """print() and str() should print the rectangle with '#'"""

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self._height):
            rectangle_str += str(self.print_symbol) * self._width + "\n"
        return rectangle_str[:-1]

    """repr() return a string of the rectangle by  using eval()"""

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    """prints a message when an instance of Rectangle is deleted"""

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """Static Method that returns the biggest Rectangle based on the area"""

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return area_2

    """ defines a class method"""

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
