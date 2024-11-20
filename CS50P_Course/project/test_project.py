import pytest
from project import check_win, get_player_move


def test_check_win():
    board_x_wins = ["X", "X", "X", " ", "O", "O", " ", " ", " "]
    board_o_wins = ["O", "O", "O", "X", "X", " ", " ", " ", " "]
    board_no_win = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]

    assert check_win(board_x_wins, "X") is True
    assert check_win(board_x_wins, "O") is False
    assert check_win(board_o_wins, "O") is True
    assert check_win(board_o_wins, "X") is False
    assert check_win(board_no_win, "X") is False
    assert check_win(board_no_win, "O") is False


def test_get_player_move(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_player_move([" "] * 9, "X") == 0

    monkeypatch.setattr('builtins.input', lambda _: "10")
    with pytest.raises(ValueError):
        get_player_move([" "] * 9, "X")
