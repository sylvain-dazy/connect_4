from src.core.game import Game
from src.desktop.view import get_cell_size, get_coordinate_of, get_grid_size


def test_cell_size():
    assert get_cell_size(10, 5) == 2 * (10 + 5)


def test_coordinate_transformation():
    assert get_coordinate_of(2, 3, 10) == (3 * 10 + 5, 2 * 10 + 5)


def test_get_grid_size():
    assert get_grid_size(Game(["Alice", "Bob"]), 10) == (7 * 10, 6 * 10)

