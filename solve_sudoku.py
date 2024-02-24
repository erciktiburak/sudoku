def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking algorithm.
    
    Args:
    - board (list of list of int): The Sudoku board representation.

    Returns:
    - bool: True if Sudoku is solved, False otherwise.
    """
    empty_cell = find_empty_location(board)
    if not empty_cell:
        return True  # Sudoku is solved
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtracking

    return False  # Sudoku cannot be solved

def is_valid(board, row, col, num):
    """
    Check if it's valid to place the given number in the specified cell.

    Args:
    - board (list of list of int): The Sudoku board representation.
    - row (int): The row index of the cell.
    - col (int): The column index of the cell.
    - num (int): The number to be placed in the cell.

    Returns:
    - bool: True if it's valid to place the number, False otherwise.
    """
    # Check if the same number exists in the same row or column
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the same number exists in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty_location(board):
    """
    Find an empty location in the Sudoku board.

    Args:
    - board (list of list of int): The Sudoku board representation.

    Returns:
    - tuple of int: The row and column indices of the empty cell, or None if not found.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return the position of the empty cell (row, col)
    return None  # No empty cell found

def print_board(board):
    """
    Print the Sudoku board.

    Args:
    - board (list of list of int): The Sudoku board representation.
    """
    for row in board:
        print(" ".join(map(str, row)))

def main():
    # Define the Sudoku board
    board = [
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

    print("Solving Sudoku:")
    if solve_sudoku(board):
        print_board(board)
    else:
        print("This Sudoku cannot be solved.")

if __name__ == "__main__":
    main()
