# Initialize the Board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]
 

def print_board(board):
    for row in board:
        print("|".join(row))
    print("-" * 5)
 
# Check for Win
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
 
# Check for Draw
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)
 
# Make Move
def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False
 
# Play the Game
def play_tic_tac_toe():
    board = initialize_board()
    current_player = 'X'
 
    print("Welcome to Tic Tac Toe!")
    print_board(board)
 
    while True:
        print(f"Player {current_player}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0-2) separated by a space: ").split())
            if 0 <= row <= 2 and 0 <= col <= 2:
                if make_move(board, row, col, current_player):
                    print_board(board)
                    if check_win(board, current_player):
                        print(f"Player {current_player} wins!")
                        break
                    elif check_draw(board):
                        print("It's a draw!")
                        break
                    current_player = 'O' if current_player == 'X' else 'X'
                else:
                    print("That spot is already taken. Try again.")
            else:
                print("Invalid input. Enter row and column between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
 
play_tic_tac_toe()