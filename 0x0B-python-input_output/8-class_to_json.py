#!/usr/bin/python3
"""Defines a class to JSON"""


def class_to_json(obj):
    """This class returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object"""

    if isinstance(obj, (str, int, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    else:
        return None
