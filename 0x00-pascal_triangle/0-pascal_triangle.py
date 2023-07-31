#!/usr/bin/python3
"""The Pascal's Triangle interview"""

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]] 

    for row in range (1, n):
        prev_row = triangle[-1]
        current_row = [1] 
        
        for i in range (1, row):
            current_row.append(prev_row[i - 1] + prev_row[i])
        
        current_row.append(1) 
        triangle.append(current_row)
    
    return triangle
