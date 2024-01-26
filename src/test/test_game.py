import pytest

from src.main.core.game import Game


@pytest.fixture
def game():
    return Game(6, 7, ("R", "Y"))


def test_new_grid_is_empty(game):
    assert game.grid == [["", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", ""]]


def test_insert_coin(game):
    game.insert_coin(0)
    assert game.grid == [["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["R", "", "", "", "", "", ""]]


def test_insert_2_coins_in_same_column(game):
    game.insert_coin(0)
    game.insert_coin(0)
    assert game.grid == [["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["Y", "", "", "", "", "", ""],
                         ["R", "", "", "", "", "", ""]]


def test_after_one_turn_restart_with_first_player(game):
    game.insert_coin(0)
    game.insert_coin(0)
    game.insert_coin(3)
    assert game.grid == [["",  "", "", "",  "", "", ""],
                         ["",  "", "", "",  "", "", ""],
                         ["",  "", "", "",  "", "", ""],
                         ["",  "", "", "",  "", "", ""],
                         ["Y", "", "", "",  "", "", ""],
                         ["R", "", "", "R", "", "", ""]]


def test_insert_3_times_in_same_col(game):
    game.insert_coin(0)
    game.insert_coin(0)
    game.insert_coin(0)
    assert game.grid == [["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["",  "", "", "", "", "", ""],
                         ["R", "", "", "", "", "", ""],
                         ["Y", "", "", "", "", "", ""],
                         ["R", "", "", "", "", "", ""]]


def test_insert_coin_in_full_column(game):
    for _ in range(6):
        game.insert_coin(0)
    with pytest.raises(Game.ColumnIsFullError):
        game.insert_coin(0)

# Tester la fin de partie
