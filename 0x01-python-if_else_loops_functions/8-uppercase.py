#!/usr/bin/python3
from ast import Num


def uppercase(str):
    i = 0
    while i < len(str):
        dig_num = ord(str[i])
        if dig_num > 96 and dig_num < 123:
            dig_num -= 32
        print(chr(dig_num), end='')
        i += 1
    print()
    return True
