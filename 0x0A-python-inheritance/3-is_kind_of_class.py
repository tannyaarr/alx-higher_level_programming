#!/usr/bin/python3
"""This defines if it is the same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """returns true if the object is an instance of a class that
        inherited directly or indirectly from the specified class"""

    return isinstance(obj, a_class)
