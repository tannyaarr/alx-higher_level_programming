#!/usr/bin/python3
"""Defines the students class using JSON"""


class Student:
    """This represents the class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize first and last name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """define to_json and return the json_data"""

        json_data = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
        }

        return json_data
