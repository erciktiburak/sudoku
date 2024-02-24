def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:
        return True  # If no empty cell, puzzle is solved
    else:
        row, col = empty_cell

    for num in range(1, 10):  # Try numbers from 1 to 9
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):  # Recursively solve Sudoku
                return True

            board[row][col] = 0  # Backtrack if no solution found

    return False  # If no number works, backtrack


def is_valid(board, row, col, num):
    # Check if num is not in the current row
    if num in board[row]:
        return False

    # Check if num is not in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if num is not in the current 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def find_empty_location(board):
    # Find and return the first empty cell (represented by 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


# Example Sudoku puzzle (0 represents empty cells)
example_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(example_board):
    print("Solution:")
    print_board(example_board)
else:
    print("No solution exists.")
