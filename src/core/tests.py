import pytest

from src.core.connect_four_checker import ConnectFourChecker
from src.core.game import Game
from src.core.grid import Grid


@pytest.fixture
def game():
    return Game("Sylvain", "Julien")


def test_first_player(game):
    assert game.get_current_player() == "Sylvain"


def test_next_player(game):
    game.play(0)
    assert game.get_current_player() == "Julien"


def test_when_last_player_played_should_be_first_player_turn(game):
    game.play(0)
    game.play(0)
    assert game.get_current_player() == "Sylvain"


def test_no_winner(game):
    assert game.get_winner() is None


def test_winner(game):
    game.play(0)
    game.play(1)
    game.play(0)
    game.play(1)
    game.play(0)
    game.play(1)
    game.play(0)
    assert game.get_winner() == "Sylvain"


def assert_winner(initial_state: list[list], expected_winner: object | None):
    for r in range(1, len(initial_state)):
        assert len(initial_state[r]) == len(initial_state[0])
    g = Grid(len(initial_state), len(initial_state[0]), initial_state=initial_state)
    checker = ConnectFourChecker(g, 4)
    assert checker.check() is expected_winner


def test_check_no_winner():
    grid = [[Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN]]
    assert_winner(grid, None)


def test_check_four_in_row():
    grid = [[Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, "R", "R", "R", "R", Grid.NO_COIN]]
    assert_winner(grid, "R")


def test_check_four_in_col():
    grid = [[Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, "R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, "R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, "R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, "R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN]]
    assert_winner(grid, "R")


def test_check_four_in_diagonal_bottom_left_to_top_right():
    grid = [[Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, "R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, "R", "Y", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, "R", "Y", "y", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            ["R",       "Y",       "Y",       "y", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN]]
    assert_winner(grid, "R")


def test_check_four_in_diagonal_top_left_to_bottom_right():
    grid = [[Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, "R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, "Y", "R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, "Y", "y", "R", Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, "Y", "Y", "Y", "R", Grid.NO_COIN]]
    assert_winner(grid, "R")


def test_bug():
    grid = [[Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            ["Y", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            ["R",       "Y", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            ["R",       "R",       "Y", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
            ["R",       "R",       "R",       "Y", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN]]
    assert_winner(grid, "Y")


@pytest.fixture
def grid():
    return Grid(6, 7)


def fill_in_column(grid, column):
    for _ in range(grid.rows):
        grid.insert("R", column)


def test_new_grids_are_empty(grid):
    assert grid.rows == 6
    assert grid.cols == 7
    assert grid.state == [[Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN]]
    assert grid.is_full() is False


def test_insert_coin(grid):
    grid.insert("R", 0)
    assert grid.state == [[Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          [Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          ["R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN]]


def test_try_inserting_in_an_invalid_column(grid):
    with pytest.raises(Grid.InvalidColumnError):
        grid.insert("R", -1)
    with pytest.raises(Grid.InvalidColumnError):
        grid.insert("R", 7)


def test_fill_in_column(grid):
    fill_in_column(grid, 0)
    assert grid.state == [["R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          ["R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          ["R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          ["R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          ["R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN],
                          ["R", Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN, Grid.NO_COIN]]


def test_grid_is_full(grid):
    assert grid.is_full() is False
    fill_in_column(grid, 0)
    fill_in_column(grid, 1)
    fill_in_column(grid, 2)
    fill_in_column(grid, 3)
    fill_in_column(grid, 4)
    fill_in_column(grid, 5)
    fill_in_column(grid, 6)
    assert grid.is_full() is True
    grid.reset()
    assert grid.is_full() is False


def test_try_inserting_in_a_full_column(grid):
    fill_in_column(grid, 0)
    with pytest.raises(Grid.ColumnFullError):
        grid.insert("R", 0)
