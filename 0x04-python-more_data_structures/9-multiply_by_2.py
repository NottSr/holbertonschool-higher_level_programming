#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    c_dictionary = a_dictionary.copy()

    for i, j in c_dictionary.items():
        c_dictionary[i] = j * 2

    return c_dictionary
