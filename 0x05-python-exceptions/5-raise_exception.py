#!/usr/bin/python3
def raise_exception():
    x = 5
    if not type(x) is str:
        raise TypeError()
