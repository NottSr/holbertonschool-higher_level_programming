#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print(i)
        break
    print("{:02d}".format(i), end=', ')
