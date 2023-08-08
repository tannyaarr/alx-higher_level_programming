#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        if ord(alphabet) >= 97 and ord(alphabet) <= 122:
            alphabet = chr(ord(alphabet) - 32)
            print("{}".format(alphabet), end="")
        else:
            print("{}".format(alphabet), end="")
