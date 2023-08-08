#!/usr/bin/python3
for num in range(0, 99):
    if num != 89 and ((num // 10) < (num % 10)):
        print("{:d}{:d}, ".format(num // 10, num % 10), end="")
    elif (num // 10) >= (num % 10):
        continue
    else:
        print("{:d}{:d}".format(num // 10, num % 10))
