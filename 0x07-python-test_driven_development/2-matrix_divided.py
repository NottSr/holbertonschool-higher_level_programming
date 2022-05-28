#!/usr/bin/python3
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
    aux = len(matrix[0])
    new_array = []
    new_matrix = []

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    for i in range(len(matrix)):

        if not aux is len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in range(len(matrix[i])):

            if not type(matrix[i][j]) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            num = matrix[i][j]
            new_array.append(round((num / div), 2))

        new_matrix.append(new_array.copy())
        new_array.clear()

    return new_matrix
