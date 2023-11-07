#!/usr/bin/python3
"""Defines the students class using JSON"""


class Student:
    """This represents the class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize first and last name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """define to_json and attrs"""

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
