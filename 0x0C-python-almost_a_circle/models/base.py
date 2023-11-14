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
    def to_json_string(list_dictionaries):
        """coverts json into string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            json_list = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """converts into a string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(4, 5, 5, 0, 0)
        elif cls.__name__ == "Square":
            dummy.instance = cls(2, 3)
        else:
            return None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a lists of instances"""
        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, "r", encoding="utf=8") as f:
                json_string = f.read()
                dictionaries  = cls.from_json_string(json_string)
                for dictionary in dictionaries:
                    instance = cls.create(**dictionary)
                    instance.append(instance)
        except FileNotFoundError:
            pass
        return instance`s
