#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    i = 1

    if (length < 2):
        # first argument is the py file ..ie ./add.py with index 0
        print("{} arguments.".format(length - 1))
    elif (length == 2):
        print("{} argument:".format(length - 1))
        print("{}: {}".format((length - 1), sys.argv[length - 1]))
    else:
        print("{} arguments:".format(length - 1))
        while(i < length):
            print("{}: {}".format((i), sys.argv[i]))
            i = i + 1
