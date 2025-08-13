from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    rows = len(board)
    cols = len(board[0])
    

    for r in range(rows):
        numbers = set()

        for c in range(cols):
            if board[r][c] in numbers:
                return False
            elif board[r][c] != ".":
                numbers.add(board[r][c])

    for c in range(cols):
        col_numbers = set()
        for r in range(rows):
            if board[r][c] in col_numbers:
                return False
            elif board[r][c] != ".":
                col_numbers.add(board[r][c])
        col_numbers = set()

    starts = [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3), (6,6),
            ]
    
    for i,j in starts:
        small_set = set()
        for r in range(i, i+3):
            for c in range(j, j+3):
                if board[r][c] in small_set:
                    return False
                elif board[r][c] != ".":
                    small_set.add(board[r][c])

    return True

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

"""