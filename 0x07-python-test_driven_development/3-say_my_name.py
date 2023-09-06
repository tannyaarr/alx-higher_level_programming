#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    if last_name:
        full_name = f"{first_name} {last_name}"
    else:
        full_name = first_name

    return full_name

