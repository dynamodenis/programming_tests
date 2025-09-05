import random

def draw_figure(board: list[list[str]], figure: list[list[str]], start_row: int, start_col: int):
    """
    Draws a 2D figure onto a larger matrix (board) at a specified position.

    Args:
        board: The larger n x m matrix, represented as a list of lists.
        figure: The smaller matrix representing the figure to be drawn.
        start_row: The row index for the top-left corner of the figure on the board.
        start_col: The column index for the top-left corner of the figure on the board.
    """
    board_rows = len(board)
    board_cols = len(board[0])
    figure_rows = len(figure)
    figure_cols = len(figure[0])

    # Check if the figure will fit on the board from the starting position
    if start_row + figure_rows > board_rows or start_col + figure_cols > board_cols:
        print("Warning: Figure is too large to fit at this position.")
        return

    # Iterate through the figure's cells and place them on the board
    for r in range(figure_rows):
        for c in range(figure_cols):
            # Only draw the character if it's not a placeholder (e.g., ' ')
            if figure[r][c] != ' ':
                board[start_row + r][start_col + c] = figure[r][c]

def print_board(board: list[list[str]]):
    """
    Prints the board in a readable format.
    """
    for row in board:
        print(" ".join(row))
    print("\n" + "-"*20 + "\n")

def can_draw(board: list[list[str]], figure: list[list[str]], start_row: int, start_col: int) -> bool:
    """
    Checks if a figure can be drawn at a given position without overlapping existing figures.
    """
    board_rows = len(board)
    board_cols = len(board[0])
    figure_rows = len(figure)
    figure_cols = len(figure[0])

    # First, check if the figure is within the board's boundaries
    if start_row + figure_rows > board_rows or start_col + figure_cols > board_cols:
        return False

    # Second, check for overlaps with existing figures on the board
    for r in range(figure_rows):
        for c in range(figure_cols):
            if figure[r][c] != ' ':
                print(f" for figure {figure} r is {r} start_row {start_row} c is {c} start_col {start_col}")
                if board[start_row + r][start_col + c] != '.':
                    return False  # Overlaps with an existing figure

    return True

# --- Main Program with updated parameters ---

def draw_figures_at_lowest_index(n: int, m: int, figures: list[list[list[str]]]):
    """
    Initializes a board of n x m and draws a list of figures at the lowest possible index.
    Each figure is placed without overlapping with previously drawn figures.

    Args:
        n: The number of rows for the board.
        m: The number of columns for the board.
        figures: A list of 2D matrices representing the figures to draw.
    """
    if n <= 0 or m <= 0:
        print("Board dimensions must be positive.")
        return
        
    board = [['.' for _ in range(m)] for _ in range(n)]
    
    print("Initial empty board:")
    print_board(board)
    
    for idx, figure in enumerate(figures):
        figure_rows = len(figure)
        figure_cols = len(figure[0])
        
        # Check if the figure can fit on the board at all
        if n < figure_rows or m < figure_cols:
            print(f"Figure {idx+1} is too large for the board and was skipped.")
            continue

        found_spot = False
        # Iterate through every possible position to find the lowest-index spot
        print(f"figure rows {figure_rows} and n is {n} iterate through how many {n - figure_rows + 1} for figure {figure}")
        for r in range(n - figure_rows + 1):
            for c in range(m - figure_cols + 1):
                if can_draw(board, figure, r, c):
                    draw_figure(board, figure, r, c)
                    found_spot = True
                    break  # Found the first spot, so break the inner loop
            if found_spot:
                break # Break the outer loop as well
        
        if found_spot:
            print(f"Board after drawing Figure {idx+1}:")
            print_board(board)
        else:
            print(f"Could not find a non-overlapping spot for Figure {idx+1}. Skipping.")
            
# Define the figures
figure_a = [['A'], ['A'], ['A'], ['A']] # I-Block
figure_b = [['B', 'B'], ['B', ' '], ['B', ' ']] # J-Block
figure_c = [['C', 'C', 'C'], [' ', 'C', ' ']] # T-Block
figure_d = [['D', ' '], ['D', ' '], ['D', 'D']] # L-Block

# Use the new function with n, m, and an array of figures
draw_figures_at_lowest_index(10, 5, [figure_a, figure_b, figure_c, figure_d])
