#!/usr/bin/python3
""" Pascal's triangle

This function generates Pascal's triangle for a given integer.

It is an arithmetic triangle in which each number is the sum of the numbers directly above it.

Args:
    n: Number of rows in the triangle.

Return:
    List of lists representing Pascal's triangle.
"""


def pascal_triangle(n):
""" Generating Pascal's triangle for a given  integer.

    Args:
        n: Number of rows in the triangle.

    Return:
        List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    first_row = [1]

    triangle.append(first_row)

    for i in range(1, n):
        row = [1]
        for j in range(len(triangle[i - 1]) - 1):
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
