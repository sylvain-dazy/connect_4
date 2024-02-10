import pytest

from src.core.grid import Grid


@pytest.fixture
def grid():
    return Grid(6, 7)


def fill_in_column(grid, column):
    for _ in range(grid.rows):
        grid.insert("R", column)


def test_new_grids_are_empty(grid):
    assert grid.rows == 6
    assert grid.cols == 7
    assert grid.state == [[Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE]]


def test_insert_coin(grid):
    grid.insert("R", 0)
    assert grid.state == [[Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          [Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          ["R",       Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE]]


def test_try_inserting_in_an_invalid_column(grid):
    with pytest.raises(Grid.InvalidColumnError):
        grid.insert("R", -1)
    with pytest.raises(Grid.InvalidColumnError):
        grid.insert("R", 7)


def test_fill_in_column(grid):
    fill_in_column(grid, 0)
    assert grid.state == [["R", Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          ["R", Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          ["R", Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          ["R", Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          ["R", Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE],
                          ["R", Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE, Grid.FREE]]


def test_try_inserting_in_a_full_column(grid):
    fill_in_column(grid, 0)
    with pytest.raises(Grid.ColumnFullError):
        grid.insert("R", 0)
