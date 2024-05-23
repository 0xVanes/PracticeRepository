import os
import random

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    clear()
    for row in board:
        print("|" + "|".join(row) + "|")
    print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return any(all(cell == player for cell in condition) for condition in win_conditions)

def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def ai_move(board, ai_player):
    player = "X" if ai_player == "O" else "O"
    for check_player in [ai_player, player]:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = check_player
                    if check_win(board, check_player):
                        return
                    board[i][j] = " "
    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if board[i][j] == " ":
            board[i][j] = ai_player
            break

def player_move(board, player):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Please enter valid row and column numbers.")

def play_game():
    board = initialize_board()
    player = "X"
    ai_player = "O"
    current_player = player

    while True:
        print_board(board)
        if current_player == player:
            player_move(board, player)
        else:
            ai_move(board, ai_player)

        if check_win(board, current_player):
            print_board(board)  # Show final board state
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)  # Show final board state
            print("It's a draw!")
            break
        current_player = ai_player if current_player == player else player

play_game()
