#!/usr/bin/python3
"""Defines a read text-file"""


def read_file(filename=""):
    """Reads a text file using UTF-8 and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
