def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "_" for num in row))

def is_valid_move(board, row, col, num):
    # Check row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    # Initialize an empty 9x9 Sudoku board
    sudoku_board = [[0 for _ in range(9)] for _ in range(9)]
    
    # Provide the initial numbers on the board (0 represents empty cells)
    # Modify this part to set up your desired Sudoku puzzle
    # Example:
    # sudoku_board = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     ...
    # ]
    
    print("Initial Sudoku Board:")
    print_board(sudoku_board)
    
    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists!")

if __name__ == "__main__":
    main()
