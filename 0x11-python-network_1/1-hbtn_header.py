#!/usr/bin/python3
"""
Takes in a URL sends a request to the URl and displays the value of the X-Request in the header
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header.get("X-Request-Id"))
