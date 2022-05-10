#!/usr/bin/python3
def no_c(my_string):
    new_str, i = '', 0
    while i < len(my_string):
        if my_string[i] != 'C' and my_string[i] != 'c':
            new_str += my_string[i]
        i += 1

    return new_str
