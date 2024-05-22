import pytest

from src.core.game import Game, InvalidColumnError, ColumnFullError

FIRST_PLAYER = "Alice"
SECOND_PLAYER = "Bob"
PLAYERS = [FIRST_PLAYER, SECOND_PLAYER]


def assert_grid_is_empty(game):
    for row in range(game.rows()):
        for col in range(game.cols()):
            assert game.get_coin_at(row, col) is None


@pytest.fixture
def game():
    return Game(PLAYERS)


def test_first_player(game):
    assert game.get_current_player() == FIRST_PLAYER


def test_grid_of_new_game_is_empty(game):
    assert game.rows() == 6
    assert game.cols() == 7
    assert_grid_is_empty(game)


def test_play_one_coin(game):
    game.play(0)
    for row in range(game.rows()):
        for col in range(game.cols()):
            if (row, col) != (5, 0):
                assert game.get_coin_at(row, col) is None


def test_after_first_player_has_played_it_is_second_player_turn(game):
    game.play(0)
    assert game.get_current_player() == SECOND_PLAYER


def test_when_second_player_has_played_then_turn_goes_to_first_player(game):
    game.play(0)
    game.play(0)
    assert game.get_current_player() == FIRST_PLAYER


def test_stack_coins_on_the_same_column(game):
    game.play(0)
    game.play(0)
    game.play(0)
    """
       0 1 2 3 4 5 6
    0 | | | | | | | |
    1 | | | | | | | |
    2 | | | | | | | |
    3 |A| | | | | | |
    4 |B| | | | | | |
    5 |A| | | | | | |
    """
    assert game.get_coin_at(5, 0) == FIRST_PLAYER
    assert game.get_coin_at(4, 0) == SECOND_PLAYER
    assert game.get_coin_at(3, 0) == FIRST_PLAYER


def test_no_winner(game):
    assert game.is_over() is False
    assert game.get_winner() is None


def test_try_inserting_in_an_invalid_column(game):
    with pytest.raises(InvalidColumnError):
        game.play(-1)
    game.play(6)
    with pytest.raises(InvalidColumnError):
        game.play(7)


def test_try_inserting_in_a_full_column(game):
    for _ in range(game.rows()):
        game.play(0)
    with pytest.raises(ColumnFullError):
        game.play(0)


def test_initially_there_is_no_winner(game):
    assert not game.is_over()
    assert game.get_winner() is None


def test_check_four_in_row(game):
    game.play(0)
    game.play(0)
    game.play(1)
    game.play(1)
    game.play(2)
    game.play(2)
    game.play(3)
    """
       0 1 2 3 4 5 6
    0 | | | | | | | |
    1 | | | | | | | |
    2 | | | | | | | |
    3 | | | | | | | |
    4 |B|B|B| | | | |
    5 |A|A|A|A| | | |
    """
    assert game.is_over()
    assert game.get_winner() is FIRST_PLAYER


def test_when_the_game_is_over_cannot_play_anymore_coins(game):
    game.play(0)
    game.play(0)
    game.play(1)
    game.play(1)
    game.play(2)
    game.play(2)
    game.play(3)
    assert game.is_over()
    game.play(4)
    """
       0 1 2 3 4 5 6
    0 | | | | | | | |
    1 | | | | | | | |
    2 | | | | | | | |
    3 | | | | | | | |
    4 |B|B|B| | | | |
    5 |A|A|A|A| | | |
    """
    assert game.get_coin_at(5, 4) is None


def test_check_four_in_col(game):
    game.play(0)
    game.play(1)
    game.play(0)
    game.play(1)
    game.play(0)
    game.play(1)
    game.play(0)
    """
       0 1 2 3 4 5 6
    0 | | | | | | | |
    1 | | | | | | | |
    2 |A| | | | | | |
    3 |A|B| | | | | |
    4 |A|B| | | | | |
    5 |A|B| | | | | |
    """
    assert game.is_over()
    assert game.get_winner() == FIRST_PLAYER


def test_check_four_in_diagonal_bottom_left_to_top_right(game):
    game.play(0)
    game.play(1)
    game.play(1)
    game.play(2)
    game.play(3)
    game.play(2)
    game.play(2)
    game.play(3)
    game.play(4)
    game.play(3)
    game.play(3)
    """
       0 1 2 3 4 5 6
    0 | | | | | | | |
    1 | | | | | | | |
    2 | | | |A| | | |
    3 | | |A|B| | | |
    4 | |A|B|B| | | |
    5 |A|B|B|A|A| | |
    """
    assert game.is_over()
    assert game.get_winner() == FIRST_PLAYER


def test_check_four_in_diagonal_top_left_to_bottom_right(game):
    game.play(6)
    game.play(5)
    game.play(5)
    game.play(4)
    game.play(4)
    game.play(3)
    game.play(4)
    game.play(3)
    game.play(2)
    game.play(3)
    game.play(3)
    """
       0 1 2 3 4 5 6
    0 | | | | | | | |
    1 | | | | | | | |
    2 | | | |A| | | |
    3 | | | |B|A| | |
    4 | | | |B|A|A| |
    5 | | |A|B|B|B|A|
    """
    assert game.is_over()
    assert game.get_winner() == FIRST_PLAYER


def test_if_grid_is_full_and_no_winner_then_game_is_over_and_it_is_a_pat(game):
    game.play(0)
    game.play(0)
    game.play(0)
    game.play(0)
    game.play(0)
    game.play(0)
    game.play(2)
    game.play(2)
    game.play(2)
    game.play(2)
    game.play(2)
    game.play(2)
    game.play(4)
    game.play(4)
    game.play(4)
    game.play(4)
    game.play(4)
    game.play(4)
    game.play(6)
    game.play(6)
    game.play(6)
    game.play(6)
    game.play(6)
    game.play(6)
    game.play(1)
    game.play(3)
    game.play(5)
    game.play(1)
    game.play(3)
    game.play(5)
    game.play(1)
    game.play(3)
    game.play(5)
    game.play(1)
    game.play(3)
    game.play(5)
    game.play(1)
    game.play(3)
    game.play(5)
    game.play(1)
    game.play(3)
    game.play(5)
    """
       0 1 2 3 4 5 6
    0 |S|S|S|F|S|S|S|
    1 |F|F|F|S|F|F|F|
    2 |S|S|S|F|S|S|S|
    3 |F|F|F|S|F|F|F|
    4 |S|S|S|F|S|S|S|
    5 |F|F|F|S|F|F|F|
    """
    assert game.get_winner() is None
    assert game.is_over()


def test_reset_winner(game):
    game.play(0)
    game.play(0)
    game.play(1)
    game.play(1)
    game.play(2)
    game.play(2)
    game.play(3)
    """
       0 1 2 3 4 5 6
    0 | | | | | | | |
    1 | | | | | | | |
    2 | | | | | | | |
    3 | | | | | | | |
    4 |B|B|B| | | | |
    5 |A|A|A|A| | | |
    """
    assert game.get_winner() is not None
    game.reset()
    assert game.get_winner() is None


def test_reset_game(game):
    game.play(0)
    game.reset()
    assert_grid_is_empty(game)
    assert game.get_current_player() == FIRST_PLAYER


def test_get_coordinate_of_last_inserted(game):
    assert game.get_coordinate_of_last_inserted() is None
    game.play(0)
    assert game.get_coordinate_of_last_inserted() == (5, 0)
    game.play(0)
    assert game.get_coordinate_of_last_inserted() == (4, 0)
    game.play(1)
    assert game.get_coordinate_of_last_inserted() == (5, 1)
