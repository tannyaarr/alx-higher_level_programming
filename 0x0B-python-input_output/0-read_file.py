#!/usr/bin/python3
"""This function reads a text file and prints it to stdout"""


def read_file(filename=""):
    """using UTF-8 and prints it to stdout"""

    with open("filename", "r", encoding="utf-8") as f:
        print(f.read(), end="")
