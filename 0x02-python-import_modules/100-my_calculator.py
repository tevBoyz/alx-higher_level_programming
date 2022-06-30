#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv[:]
    argc = len(argv)

    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, *, and /')
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]

        if op == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif op == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        exit(0)
