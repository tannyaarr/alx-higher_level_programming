#!/usr/bin/python3
"""Defines the JSON function"""


import json
"""import the json module"""


def to_json_string(my_obj):
    """returns the JSON representation of an object(string)"""

    return json.dumps(my_obj)
