#!/usr/bin/python3
num = 122
while num != 65:
    print(chr(num), end='')
    if num < 91:
        num += 31
    else:
        num -= 33
print(chr(num), end='')
