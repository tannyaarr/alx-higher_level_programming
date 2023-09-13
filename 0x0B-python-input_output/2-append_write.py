#!/usr/bin/python3
"""Defines a function that appends a string in a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns
        number of characters added"""

    with open(filename, 'a', encoding='utf-8') as f:
        char_count = f.write(text)
        return char_count
