from typing import List
"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:

        # Add all in the first row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # Get everything in i which is the last in the right column
        for i in range (top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        # When we get to the end break and start new row
        if not (left < right and top < bottom):
            break
        # add everyting from the bottom
        for i in range(right -1, left - 1, -1):
            res.append(matrix[bottom -1][i])
        bottom -= 1
        # for i in the left col
        for i in range(bottom -1, top -1, -1):
            res.append(matrix[i][left])
        left += 1

    return res

results = spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(f"result {results}")
