#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not all(all(isinstance(e, (int, float)) for e in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(e / div, 2) for e in row] for row in matrix]

    return result_matrix
