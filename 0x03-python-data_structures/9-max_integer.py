#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_v = min(my_list)
    for i in my_list:
        if i > max_v:
            max_v = i

    return max_v
