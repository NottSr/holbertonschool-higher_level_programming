#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 3))
except TypeError as te:
    print(te)

print(matrix)

matrix = [
    [1, "a", 3],
    [4, 5, "b"],
    ["c", 8, 9]
]
try:
    print(matrix_divided(matrix, 3))
except TypeError as te:
    print(te)

print(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6, 7, 8]
]
try:
    print(matrix_divided(matrix, 3))
except TypeError as te:
    print(te)

print(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 0))
except ZeroDivisionError as ze:
    print(ze)

print(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, "a"))
except TypeError as te:
    print(te)

print(matrix)
