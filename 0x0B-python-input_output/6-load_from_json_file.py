#!/usr/bin/python3
"""Defines the JSON module by creating a object"""


import json
"""import the json module"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data
