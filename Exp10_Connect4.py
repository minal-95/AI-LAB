def create_board():
    return [[0 for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print(' '.join(str(x) for x in row))
    print("1 2 3 4 5 6 7")  # Column numbers for reference

def valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for r in range(5, -1, -1):  # Start from bottom row
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        print_board(board)
        # Ask for Player 1 Input
        if turn == 0:
            col = int(input("Player 1 Make Your Selection (1-7):")) - 1

            if valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print_board(board)
                    print("Player 1 Wins!")
                    game_over = True

        # Ask for Player 2 Input
        else:
            col = int(input("Player 2 Make Your Selection (1-7):")) - 1

            if valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print_board(board)
                    print("Player 2 Wins!")
                    game_over = True

        turn += 1
        turn = turn % 2

if __name__ == "__main__":
    play_game()

