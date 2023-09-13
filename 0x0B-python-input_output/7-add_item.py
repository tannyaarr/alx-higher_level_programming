#!/usr/bin/python3
import sys
import os
import json
"""import sys and os  module"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    if os.path.isfile('add_item.json'):
        data = load_from_json_file('add_item.json')
    else:
        data = []

    data.extend(sys.argv[1:])

    save_to_json_file(data, 'add_item.json')


if __name__ == "__main__":
    main()
