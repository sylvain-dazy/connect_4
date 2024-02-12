from src.core.game import Game


def test_first_player():
    game = Game("Sylvain", "Julien")
    assert game.get_current_player() == "Sylvain"


def test_next_player():
    game = Game("Sylvain", "Julien")
    game.play(0)
    assert game.get_current_player() == "Julien"


def test_when_last_player_played_should_be_first_player_turn():
    game = Game("Sylvain", "Julien")
    game.play(0)
    game.play(0)
    assert game.get_current_player() == "Sylvain"