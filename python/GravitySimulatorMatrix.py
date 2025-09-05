from typing import List


def solution(board: List[List[str]]):
    """
    Simulates falling boxes and exploding obstacles on a rectangular board.

    Boxes ('#') fall simultaneously as far as possible until they hit an obstacle ('*')
    or the bottom of the board. Obstacles are considered fixed barriers.
    If a falling box hits an obstacle, both explode, destroying themselves and
    any other boxes ('#') within an 8-cell radius around the obstacle (a 3x3 grid centered
    at the obstacle, excluding the hitting box as it's handled separately).
    All explosions and their effects happen simultaneously after all boxes have fallen.

    Args:
        board: A list of lists of strings representing the board.
               Each cell contains '.', '*', or '#'.

    Returns:
        The new board after all boxes have fallen and explosions have occurred.
    """

    rows = len(board)
    cols = len(board[0])

    # Phase 1: Simulate Falling Boxes
    # Boxes fall down each column. Obstacles are fixed in their column.
    # We can effectively "compact" each column.
    board_after_fall = [["_" for _ in range(cols)] for _ in range(rows)]
    final_board = [["_" for _ in range(cols)] for _ in range(rows)]

    # The reason why we are not startting with row then column is because we want to process columns of each row.
    # More like start with column top to down
    for j in range(cols):
        column_elements = []
        for i in range(rows):
            if board[i][j] != "_":
                column_elements.append(board[i][j])
        print(f"Column elements {column_elements} for col {j}")
        # Place these elements back into the column, starting from the bottom
        # and filling upwards. Empty cells will remain at the top.

        current_idx_in_elements = (
            len(column_elements) - 1
        )  # for us to start from the last elemnt
        for i in range(rows - 1, -1, -1):
            if current_idx_in_elements >= 0:
                board_after_fall[i][j] = column_elements[current_idx_in_elements]
                current_idx_in_elements -= 1
            else:
                board_after_fall[i][j] = "_"
    
    # Identitfy explosion centers
    # Set to store(rows, col) cordinates of obstacles that are hit by the box
    explosion_centers = set()
    for i in range(rows):
        for j in range(cols):
            # An Obstacle is hit if its currently an "*" and the cel directly above it a "#"
            if (
                board_after_fall[i][j] == "*"
                and i > 0
                and board_after_fall[i - 1][j] == "#"
            ):
                explosion_centers.add((i, j))

    print(f"explosion points {explosion_centers}")

    # Add the explosions
    # Store all records that will be destroyed and means turning to _
    cells_to_destroy = set()

    for exp_r, exp_c in explosion_centers:
        # The obstacle will be hit and destroyed
        cells_to_destroy.add(
            (exp_r, exp_c)
        )  # This part here destroys the obstacle but we should not destroy the obstacle
        # The obstacle directly above the obstacle will hit the obstacle and will be destroyed
        cells_to_destroy.add((exp_r - 1, exp_c))
        
        # Destroy all boxes within the 8-cell radius  around the obstacle meaning a 3*3 centered around obstacle exp_r, exp_c
        print(f"exp_r -1 {exp_r -1 } and expr + 2 {exp_r + 2}")
        for dr in range(exp_r - 1, exp_r + 2):
            for dc in range(exp_c - 1, exp_c + 2):
                # Ensure coordinates are witin the board boundaries
                if 0 <= dr < rows and 0 <= dc < cols:
                    # Only destroy obstacles in the radius but obstacles are not destroyed only boxes
                    if board_after_fall[dr][dc] == "#":
                        cells_to_destroy.add((dr, dc))
        print(f"cells to destroy {cells_to_destroy}")

        for i in range(rows):
            for j in range(cols):
                if (i, j) in cells_to_destroy:
                    final_board[i][j] = "_"
                else:
                    # Kepp the elements after falling
                    final_board[i][j] = board_after_fall[i][j]
    return final_board


board_example = [
    ["_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_"],
    ["_", "#", "_", "_", "#", "_"],
    ["_", "_", "_", "_", "_", "_"],
    ["_", "*", "_", "*", "_", "_"],
]
print("Original Board (Example 1):")
for row in board_example:
    print(row)

result_board_example = solution(board_example)

print("\nResult Board (Example 1) after simulation:")
for row in result_board_example:
    print(row)
