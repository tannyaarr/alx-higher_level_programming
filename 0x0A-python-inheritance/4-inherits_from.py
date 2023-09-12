#!/usr/bin/python3
"""This defines the inherits_from def"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that
        inherited directly or indrectly from the specfied class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
