from typing import List
"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""


def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    result = [] # flaten or put them all in 1 array
    rows = len(mat)
    cols = len(mat[0])

    output = [[0 for _ in range(c)] for _ in range(r)] # structure of the new matrix filled with 0
    
    if rows * cols != r * c:
        return mat

    for i in range(rows):
        for j in range(cols):
            result.append(mat[i][j])
            
    k = 0
    for i in range(r):
        for j in range(c):
            output[i][j] = result[k]
            k += 1


    return output