#!/usr/bin/python3
"""Defines the class MyList"""


class MyList(list):
    """This represents MyList class"""

    def __init__(self):
        """Instatiation of MyList class"""
        list.__init__(self)

    def print_sorted(self):
            print(sorted(self))
