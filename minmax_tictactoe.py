class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board represented as 1D array
        self.current_winner = None


    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def print_board_nums():
        # Shows what number corresponds to what spot
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']


    def empty_squares(self):
        return ' ' in self.board


    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False


    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True


        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True


        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True


        return False


def minimax(game, maximizing):
    # Base cases - terminal states
    if game.current_winner:
        if maximizing:
            return {'position': None, 'score': -1}  # X wins
        else:
            return {'position': None, 'score': 1}   # O wins
    elif not game.empty_squares():
        return {'position': None, 'score': 0}   # Tie


    if maximizing:  # Maximizing player (X)
        best = {'position': None, 'score': -float('inf')}
        letter = 'X'
    else:  # Minimizing player (O)
        best = {'position': None, 'score': float('inf')}
        letter = 'O'


    for possible_move in game.available_moves():
        # Make a move
        game.make_move(possible_move, letter)
        
        # Recursively get the score
        sim_score = minimax(game, not maximizing)
        
        # Undo the move
        game.board[possible_move] = ' '
        game.current_winner = None
        
        sim_score['position'] = possible_move


        if maximizing:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score


    return best


def play_game():
    game = TicTacToe()
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered as follows:")
    game.print_board_nums()


    while game.empty_squares():
        # Human player (O)
        valid_move = False
        while not valid_move:
            try:
                square = int(input("Enter your move (0-8): "))
                valid_move = game.make_move(square, 'O')
                if not valid_move:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 0 and 8.")


        game.print_board()
        if game.current_winner:
            print("O wins!")
            break
        
        if not game.empty_squares():
            print("It's a tie!")
            break


        # AI player (X)
        print("AI is thinking...")
        ai_move = minimax(game, True)['position']
        game.make_move(ai_move, 'X')
        print(f"AI chose position {ai_move}")
        game.print_board()
        
        if game.current_winner:
            print("X wins!")
            break


if __name__ == '__main__':
    play_game()


