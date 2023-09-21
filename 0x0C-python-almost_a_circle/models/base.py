#!/usr/bin/python3
"""This is the creation of the Base class"""


import json
"""import the module json"""


class Base:
    """This defines the class Base"""

    __nb_objects = 0
    """private attribute"""

    def __init__(self, id=None):
        """Initializes the id which is equal to None"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    """Static method that returns the JSON string representation of a list
    of dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries to be converted
            to a JSON string

        Returns:
            str: The JSON strin representation of the input list

        Note:
            If the input list is None or empty, the method returns "[]"

    """

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    """Class method that writes the JSON string representation of list_objs
    to a file"""

    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            json_string = cla.to_json_string([obj.to_dictionary()
                for obj in list_objs])
            f.write(json_string)

    @staticmethod
    """Static method that returns list of JSON string representation
    json_string"""

    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    """Returns an instance with attributes already set"""

    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ = 'Square':
            dummy.instance = cls(1)
        else:
            return None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    """Adding the class method def load_from_file(cls) that returns a list
    of instances"""

    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionaries = cls.from_json_string(json_string)
                for dictionary in dictionaries:
                    instance = cls.create(**dictionary)
                    instance.append(instance)
        except FileNotFoundError:
            pass
        return instances
