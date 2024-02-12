from src.core.connect_four_checker import ConnectFourChecker
from src.core.grid import Grid


class Game:
    def __init__(self, first: str, second: str):
        self.winner = None
        self.players = [first, second]
        self.current_player = 0
        self.grid = Grid(6, 7)
        self.connect_four_checker = ConnectFourChecker(self.grid)

    def get_current_player(self):
        return self.players[self.current_player]

    def play(self, column: int):
        self.grid.insert(self.current_player, column)
        self.winner = self.connect_four_checker.check()
        self.current_player = self.next_player()

    def next_player(self):
        return (self.current_player + 1) % len(self.players)

    def get_winner(self):
        if self.winner is not None:
            return self.players[self.winner]
        return None
