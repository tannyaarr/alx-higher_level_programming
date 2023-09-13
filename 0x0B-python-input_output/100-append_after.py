#!/usr/bin/python3
"""Defines the append search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line a text to a file after each line containing
        a specific string"""

    if not filename:
        return

    with open(filename, 'r', encoding='utf-8') as r:
            lines = f.realines()

    with open(filename, 'w', encoding='utf-8') as w:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
