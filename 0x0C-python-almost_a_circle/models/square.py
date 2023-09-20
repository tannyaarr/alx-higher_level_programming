#!/usr/bin/python3
"""This defines Square inherited from Rectangle"""


class Square(Rectangle):
    """This defines the inherited Square from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialzation of the Rectangle class"""

        super()__init__(size, size, x, y, id)

    @property
    """Updates the Square by adding a public getter and setter for size
    attribute and ensures that the setter assigns same value to both width
    and height"""

    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        self.width  value

    def update(self,* args, **kwargs):
        """updates the Square and assigns attributes"""

        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], args)
        else:
            for key, value in kwargs.items():
                setattr(self. key, value)
    def to_dictionay(self):

        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.__size,
            'x': self.__x,
            'y': self.__y
        }

    def __str__(self):
        """ the __str__ method is overridden to return the string
        representation of the Square"""

        return f"[Square] {(self.id)} {self.x}/{self.y} - {self.width}"
