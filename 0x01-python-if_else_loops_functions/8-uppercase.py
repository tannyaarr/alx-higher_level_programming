#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('A') >= ord(char) <= ord('Z'):
            return True
        else:
            return False
