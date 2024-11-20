def main():
    board = [" "] * 9
    current_player = "X"
    while True:
        print_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif " " not in board:
            print_board(board)
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"


def print_board(board):
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---------")


def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != " ":
                raise ValueError
            return move
        except ValueError:
            print("Invalid move. Try again.")


def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)


if __name__ == "__main__":
    main()
