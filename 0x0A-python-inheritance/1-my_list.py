#!/usr/bin/python3
"""Defines the class MyList"""


class MyList(list):
    """This represents MyList class"""

    def print_sorted(self):
        """Prints a list in sorted ascending order"""
        print(sorted(self))
