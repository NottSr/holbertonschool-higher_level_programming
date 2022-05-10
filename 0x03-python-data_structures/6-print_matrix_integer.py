#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for vals in matrix:
            i, length = 1, len(vals)

            for val in vals:
                if i == length:
                    print('{:d}'.format(val), end='')
                else:
                    print('{:d}'.format(val), end=' ')
                i += 1

            print()
