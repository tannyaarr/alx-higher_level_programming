#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv))
    if len(argc) != 4:
        print('Usage: {}  <a> <operator> <b>'.format(argv[0]))
        exit(1)
    ops = {
        '+': add, 
        '-': sub, 
        '*': mul, 
        '/': div
    }
    if argv[2] in ops:
        a = int(argv[1])
        op = ops[argv[2]]
        b = int(argv[3])
        result = op(a, b)
        print('{:d} {:s} {:d} = {:d}'.format(a, argv[2], b, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
        
