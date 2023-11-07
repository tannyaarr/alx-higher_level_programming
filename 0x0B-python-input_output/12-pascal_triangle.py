#!/usr/bin/python3
"""Defines the Pascal Triangle function"""


def pascal_triangle(n):
    """Returns a list of a lists of integers representing the Pascal's
        triangle of n"""

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
        triangle.append(row)
    return triangle
