#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    i = 1

    ss = ''
    if argc == 0:
        ss = 's.'
    elif argc == 1:
        ss = ':'
    else:
        ss = 's:'

    print("{:d} argument{:s}".format(argc, ss))

    while i <= argc:
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
