def is_safe(board, row, col, n):
    """Checks if placing a queen at (row, col) is safe."""
    for i in range(row): # only checks the rows above current row
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False
    return True
 
def print_board(board):
    """Prints the board."""
    print('\n'.join(' '.join('Q' if c else '.' for c in row) for row in board), '\n')
 
def solve_n_queens(n):
    """Solves N Queens with manual placements."""
    board = [[0] * n for _ in range(n)]
 
    while True:
        try:
            num_manual = int(input(f"Manual queens (0-{n}): "))
            if 0 <= num_manual <= n:
                break
            print(f"Enter 0-{n}.")
        except ValueError:
            print("Invalid input.")
 
    for i in range(num_manual):
        while True:
            try:
                r, c = map(int, input(f"Queen {i+1} (row col): ").split())
                if 0 <= r < n and 0 <= c < n:
                    if board[r][c] or not is_safe(board, r, c, n):
                        print("Unsafe/Occupied. Try again.")
                        continue
                    board[r][c] = 1
                    print(f"Board ({i+1} placed):")
                    print_board(board)
                    break
                print(f"Row/Col 0-{n-1}.")
            except (ValueError, IndexError):
                print("Invalid row col format.")
 
    def solve_recursive(board, row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(board, row, col, n):
                temp = board[row][col]
                board[row][col] = 1
                if solve_recursive(board, row + 1):
                    return True
                board[row][col] = temp
        return False
 
    if solve_recursive(board, 0):
        return board
    return None
 
while True:
    try:
        n = int(input("Board size (N): "))
        if n > 0:
            break
        print("Positive integer please.")
    except ValueError:
        print("Invalid input.")
 
solution = solve_n_queens(n)
if solution:
    print("Final Solution:")
    print_board(solution)
else:
    print("No solution.")