#!/usr/bin/python3
"""Defines the JSON module by writing an object to a text file"""


import json
"""imports the json module"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file using JSON representation"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False, indent=4)
