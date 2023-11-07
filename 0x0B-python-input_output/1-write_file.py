#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to text file and returns the number of
        characters written"""

    with open(filename, 'w', encoding='utf-8') as f:
        char_count = f.write(text)
        return char_count
