#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i, sum = 1, 0

    while i < len(argv):
        sum += int(argv[i])
        i += 1

    print(sum)
