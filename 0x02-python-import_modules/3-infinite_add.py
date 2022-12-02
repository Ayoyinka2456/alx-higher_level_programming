#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    length = len(sys.argv)
    counter = 1
    total = 0

    if (length == 1):
        print(0)
    else:
        while (counter < length):
            total = total + int(sys.argv[counter])
            counter += 1
        print(total)
