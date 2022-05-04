#!/usr/bin/python3
def print_last_digit(number):
    last_dig = int(repr(number)[-1])
    print(last_dig, end='')
    return last_dig
