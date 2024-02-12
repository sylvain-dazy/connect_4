from src.core.grid import Grid


class Game:
    def __init__(self, first: str, second: str):
        self.players = [first, second]
        self.current_player = 0
        self.grid = Grid(6, 7)

    def get_current_player(self):
        return self.players[self.current_player]

    def play(self, column: int):
        self.grid.insert(self.current_player, column)
        self.current_player = self.next_player()

    def next_player(self):
        return (self.current_player + 1) % len(self.players)


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
