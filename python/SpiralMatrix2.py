from typing import List

"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Input: n = 1
Output: [[1]]

"""

def generateMatrix(n: int) -> List[List[int]]:
    rows = n
    cols = n
    structure = [[0 for _ in range(cols)] for _ in range(rows)]


    left, right = 0, cols - 1
    top, bottom = 0, rows - 1

    index = 1

    print(f"Left {left} right {right}")
    print(f"Top {top} bottom {bottom}")

    while top <= bottom:
        # Add the firt row 
        for i in range(top, right + 1):
            structure[top][i] = index
            index += 1
        top += 1

        # Add records in the right
        for i in range(top, bottom + 1):
            structure[i][right] = index
            index += 1
        right -= 1

        #Add records in bottom
        for i in range(right, left -1, -1):
            structure[bottom][i] = index
            index += 1
        bottom -= 1

        #Add left records
        for i in range(bottom, top -1, -1):
            print(f"i in {i}")
            structure[i][left] = index
            index += 1
        left += 1

    print(f"new strucure {structure}")
    return structure
        