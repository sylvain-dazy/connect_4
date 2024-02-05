import pytest

from src.core.game import Game


@pytest.fixture
def game():
    return Game()


def test_switch_between_player(game):
    assert game.current_player == 0
    assert game.get_current_player() == "R"
    game.next_player()
    assert game.current_player == 1
    assert game.get_current_player() == "Y"
    game.next_player()
    assert game.current_player == 0
    assert game.get_current_player() == "R"
