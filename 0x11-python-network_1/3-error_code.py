#!/usr/bin/python3
""" Error code"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except:
        print(f"Error code: {e.code}")

