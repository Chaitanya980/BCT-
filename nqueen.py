def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        # All queens are placed, print the board
        for i in range(n):
            print(board[i])
        print("\n")
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n)
            board[row][col] = 0  # Backtrack

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

n_queens(4)