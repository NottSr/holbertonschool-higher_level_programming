#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = 1
    if len(argv) == 1:
        print(f"{len(argv) - 1} arguments.")
    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments:")

    while i < len(argv):
        print(f"{i}: {argv[i]}")
        i += 1
