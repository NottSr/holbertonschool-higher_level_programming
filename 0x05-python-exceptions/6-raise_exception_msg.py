#!/usr/bin/python3
def raise_exception_msg(message=""):
    if not type(message) is int:
        raise NameError(message)
