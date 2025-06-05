import random

def create_board():
    return [['-' for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print('0 1 2 3 4 5 6')

def is_valid_column(board, col):
    return board[0][col] == '-'

def get_next_open_row(board, col):
    for row in reversed(range(6)):
        if board[row][col] == '-':
            return row
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def check_win(board, piece):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if board[row][col] == piece and board[row][col+1] == piece and \
               board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    # Check vertical
    for row in range(3):
        for col in range(7):
            if board[row][col] == piece and board[row+1][col] == piece and \
               board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    return False

def is_draw(board):
    return all(cell != '-' for cell in board[0])

def get_valid_columns(board):
    return [col for col in range(7) if is_valid_column(board, col)]

def player_move(board):
    while True:
        try:
            col = int(input("Enter your move (0-6): "))
            if col < 0 or col > 6:
                print("Column out of range. Try again.")
            elif not is_valid_column(board, col):
                print("Column is full. Try another one.")
            else:
                return col
        except ValueError:
            print("Invalid input. Enter a number between 0 and 6.")

def simulate_move(board, col, piece):
    temp_board = [row[:] for row in board]  # Deep copy
    row = get_next_open_row(temp_board, col)
    if row is not None:
        drop_piece(temp_board, row, col, piece)
    return temp_board

def computer_move(board):
    valid_columns = get_valid_columns(board)

    # 1. Try to win
    for col in valid_columns:
        temp_board = simulate_move(board, col, 'O')
        if check_win(temp_board, 'O'):
            return col

    # 2. Try to block player
    for col in valid_columns:
        temp_board = simulate_move(board, col, 'X')
        if check_win(temp_board, 'X'):
            return col

    # 3. Else pick center if possible
    if 3 in valid_columns:
        return 3

    # 4. Else random
    return random.choice(valid_columns)

def main():
    print("Welcome to Connect 4 (Human vs Computer)!")

    while True:
        board = create_board()
        game_over = False
        turn = 0  # 0 for player, 1 for computer

        print_board(board)

        while not game_over:
            if turn == 0:
                col = player_move(board)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 'X')

                if check_win(board, 'X'):
                    print_board(board)
                    print("Congratulations! You win!")
                    game_over = True
                else:
                    turn = 1
            else:
                print("Computer is making a move...")
                col = computer_move(board)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 'O')

                if check_win(board, 'O'):
                    print_board(board)
                    print("Computer wins. Better luck next time!")
                    game_over = True
                else:
                    turn = 0

            print_board(board)

            if is_draw(board) and not game_over:
                print("It's a draw!")
                game_over = True

        # Ask if user wants to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()