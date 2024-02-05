import pytest

from src.core.board import Grid


@pytest.fixture
def grid():
    return Grid(6, 7)


def test_new_grid_should_be_empty(grid):
    expected = [["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]]
    assert grid.state == expected
    assert grid.is_full() is False
    for row in range(grid.rows):
        for col in range(grid.cols):
            assert grid.is_free(row, col)


def test_insert_coin(grid):
    grid.insert_coin("R", 0)
    expected = [["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["R", "", "", "", "", "", ""]]
    assert grid.state == expected


def test_insert_coins_in_same_column(grid):
    grid.insert_coin("R", 0)
    grid.insert_coin("Y", 0)
    expected = [["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["",  "", "", "", "", "", ""],
                ["Y", "", "", "", "", "", ""],
                ["R", "", "", "", "", "", ""]]
    assert grid.state == expected


def test_insert_coin_in_full_column(grid):
    for _ in range(grid.rows):
        grid.insert_coin("R",0)
    with pytest.raises(Grid.ColumnIsFullError):
        grid.insert_coin("R", 0)
