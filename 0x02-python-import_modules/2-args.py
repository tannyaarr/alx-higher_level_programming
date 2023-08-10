#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_count = len(sys.argv) - 1
    if args_count == 0:
        print('0 arguments.')
    else:
        if args_count == 1:
            print('1 argument:')
        else:
            print('{} arguments:'.format(args_count))

    for i, arg in  enumerate(sys.argv[1:], start=1):
            print('{}: {}'.format(i, arg))
