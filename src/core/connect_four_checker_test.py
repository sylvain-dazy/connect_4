from src.core.connect_four_checker import ConnectFourChecker
from src.core.grid import Grid


def assert_winner(initial_state: list[list], expected_winner: object | None):
    g = Grid(initial_state=initial_state)
    checker = ConnectFourChecker(g)
    assert checker.check() is expected_winner


def test_check_no_winner():
    grid = [[Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE]]
    assert_winner(grid, None)


def test_check_four_in_row():
    grid = [[Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, "R", "R", "R", "R", Grid.FREE]]
    assert_winner(grid, "R")


def test_check_four_in_col():
    grid = [[Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, "R", Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, "R", Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, "R", Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, "R", Grid.FREE, Grid.FREE, Grid.FREE]]
    assert_winner(grid, "R")


def test_check_four_in_diagonal_bottom_left_to_top_right():
    grid = [[Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, "R", Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, "R",       "Y", Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, "R",       "Y",       "y", Grid.FREE, Grid.FREE, Grid.FREE],
            ["R",       "Y",       "Y",       "y", Grid.FREE, Grid.FREE, Grid.FREE]]
    assert_winner(grid, "R")


def test_check_four_in_diagonal_top_left_to_bottom_right():
    grid = [[Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, "R", Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, "Y",       "R", Grid.FREE, Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, "Y",       "y",       "R", Grid.FREE, Grid.FREE],
            [Grid.FREE, Grid.FREE, "Y",       "Y",       "Y",       "R", Grid.FREE]]
    assert_winner(grid, "R")
