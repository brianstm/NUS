# Tic-Tac-Toe

#### Video Demo: XXX

#### Description:

This project is a command-line implementation of the classic game Tic-Tac-Toe, where two players compete to align their marks (X or O) on a 3x3 grid. Each player takes turns selecting a cell, marked numerically from 1 (top-left) to 9 (bottom-right), to place their symbol. The first player to achieve a horizontal, vertical, or diagonal sequence of three marks wins the game. If all cells are filled and neither player has achieved alignment, the game ends in a tie.

The game is structured with a clear set of functions to guide gameplay and ensure functionality:

- **`main()` function**: This core function initializes the game, facilitates the turns between players, and determines when the game should end, either through a win or a draw.
- **`print_board()` function**: Displays the current state of the board after each turn, providing a clear view of each player’s progress and the overall game status.
- **`get_player_move()` function**: Prompts players to enter a cell number for their move. It validates the input to ensure that the selected cell is available and within range, adding a layer of user-friendly error checking.
- **`check_win()` function**: An essential part of the game logic, this function checks the board after each move to see if there’s a winning alignment. If a win is detected, the game promptly ends, declaring the winning player.

To ensure it's reliability, the project includes unit tests in `test_project.py` that rigorously validate critical functions. These tests cover edge cases for the `check_win()` function, confirming accurate detection of winning conditions, as well as the `get_player_move()` function, ensuring it correctly handles input validation.
