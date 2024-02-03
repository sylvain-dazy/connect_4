import pytest

from src.main.core.board import Board
from src.main.core.game import Game


@pytest.fixture
def game():
    return Game(6, 7, ("R", "Y"))


def assert_game_state(game, expected):
    assert game.board.grid == expected


def test_new_grid_is_empty(game):
    expected = [["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]]
    assert_game_state(game, expected)


def test_insert_coin(game):
    game.insert_coin(0)
    expected = [["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["R", "", "", "", "", "", ""]]
    assert_game_state(game, expected)


def test_insert_2_coins_in_same_column(game):
    game.insert_coin(0)
    game.insert_coin(0)
    expected = [["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["Y", "", "", "", "", "", ""],
                ["R", "", "", "", "", "", ""]]
    assert_game_state(game, expected)


def test_after_one_turn_restart_with_first_player(game):
    game.insert_coin(0)
    game.insert_coin(0)
    game.insert_coin(3)
    expected = [["",  "", "", "",  "", "", ""],
                ["",  "", "", "",  "", "", ""],
                ["",  "", "", "",  "", "", ""],
                ["",  "", "", "",  "", "", ""],
                ["Y", "", "", "",  "", "", ""],
                ["R", "", "", "R", "", "", ""]]
    assert_game_state(game, expected)


def test_insert_3_times_in_same_col(game):
    game.insert_coin(0)
    game.insert_coin(0)
    game.insert_coin(0)
    expected = [["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["R", "", "", "", "", "", ""],
                ["Y", "", "", "", "", "", ""],
                ["R", "", "", "", "", "", ""]]
    assert_game_state(game, expected)


def test_insert_coin_in_full_column(game):
    for _ in range(6):
        game.insert_coin(0)
    with pytest.raises(Board.ColumnIsFullError):
        game.insert_coin(0)
