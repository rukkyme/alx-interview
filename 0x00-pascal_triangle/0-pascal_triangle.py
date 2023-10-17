#!/usr/bin/python3
"""The Pascal's Triangle interview"""

def pascal_triangle(n):
	pascal_t = []
    for i in range(1, n + 1):
        row = [1] * (i)
        for j in range(2, i):
            row[j - 1] = pascal_t[i - 2][j - 2] + pascal_t[i - 2][j - 1]
        pascal_t.append(row)
    return pascal_t
