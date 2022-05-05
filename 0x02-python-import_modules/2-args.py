#!/usr/bin/python3
import sys
i = 1
print(f"{len(sys.argv) - 1} arguments", end='')

if len(sys.argv) == 1:
    print(".")
else:
    print(":")

while i < len(sys.argv):
    print(f"{i}: {sys.argv[i]}")
    i += 1
