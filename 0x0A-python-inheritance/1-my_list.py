#!/usr/bin/python3
"""Defines the class MyList"""


class MyList(list):
    """This represents MyList class"""
    def print_sorted(self):
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end=' ')
        print()
