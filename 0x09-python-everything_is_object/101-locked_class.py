#!/usr/bin/python3
"""Defines the class LockedClass"""


class LockedClass:

    """This represents the class LockedClass"""

    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{}'")
