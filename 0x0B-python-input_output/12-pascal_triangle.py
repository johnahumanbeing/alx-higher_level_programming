#!/usr/bin/python3
"""Define pascal_triangle"""


def pascal_triangle(n):
    """Defining pascal_triangle
    returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    pas_triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pas_triangle[i-1][j-1] + pas_triangle[i-1][j])
        row.append(1)
        pas_triangle.append(row)

    return pas_triangle
