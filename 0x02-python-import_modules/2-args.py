#!/usr/bin/python3
from sys import argv
i = 1
print(f"{len(argv) - 1} arguments", end='')

if len(argv) == 1:
    print(".")
else:
    print(":")

while i < len(argv):
    print(f"{i}: {argv[i]}")
    i += 1