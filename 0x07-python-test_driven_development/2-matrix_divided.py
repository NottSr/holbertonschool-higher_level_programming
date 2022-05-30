#!/usr/bin/python3
"""
Module that checks for a NaN value
"""


def isNaN(num):
    """
    Returns:
        True if value is NaN
    """
    return num != num


"""
Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: A matrix full of integers and floats
        div: integer or float number

    Raises:
        ZeroDivisionError: If var div is 0
        TypeError: If var div is not an integer or float
        TypeError: If each row of the matrix have not the same size
        TypeError: If matrix is not a matrix full of int of floats

    Returns:
        new_matrix: A new matrix with the div results
    """
    new_array = []
    new_matrix = []

    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    aux = len(matrix[0])

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not type(div) in (int, float) or isNaN(div) is True:
        raise TypeError("div must be a number")

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if not type(matrix[i][j]) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            if aux is not len(matrix[i]):
                raise TypeError("Each row of the matrix must have the same size")

            num = matrix[i][j]
            new_array.append(round((num / div), 2))

        new_matrix.append(new_array.copy())
        new_array.clear()

    return new_matrix
