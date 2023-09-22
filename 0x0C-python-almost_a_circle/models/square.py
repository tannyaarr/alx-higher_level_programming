#!/usr/bin/python3
"""This defines Square inherited from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """This defines the inherited Square from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialzation of the Rectangle class"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """public getter and setter size""" 
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self,* args, **kwargs):
        """updates the Square and assigns attributes"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return the string representation of the Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
