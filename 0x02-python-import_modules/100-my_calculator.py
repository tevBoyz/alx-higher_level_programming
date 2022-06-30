#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv[1:]
    argc = len(argv)

    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif argv[1] not in '+-*/':
        print('Unknown operator. Available operators: +, -, *, and /')
        exit(1)
    else:
        a = int(argv[0])
        b = int(argv[2])
        op = argv[1]

        if op == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif op == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
