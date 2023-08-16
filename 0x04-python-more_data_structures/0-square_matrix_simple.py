#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = [value ** 2 for value in row]
        squared_matrix.append(squared_row)
    return squared_matrix
