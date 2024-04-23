import random

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
        print("-------")

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def check_win(board, player):
    # Check horizontal and vertical
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def play_game():
    board = initialize_board()
    current_player = 'X' if random.choice([True, False]) else 'O'

    while True:
        print(f"Current board:")
        print_board(board)
        print(f"Player {current_player}'s turn.")

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the spot is valid
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Invalid move, try again.")
            continue

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full
        if is_board_full(board):
            print_board(board)
            print("The game is a draw.")
            break

        # Switch player
        current_player = 'X' if current_player == 'O' else 'O'

    print("Final board:")
    print_board(board)

# Main function to start the game
if __name__ == "__main__":
    play_game()
