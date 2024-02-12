from src.core.connect_four_checker import ConnectFourChecker
from src.core.grid import Grid


class Game:

    def __init__(self, rows: int = 6, cols: int = 7, players: tuple[str, str] = ("R", "Y")):
        self.current_player = 0
        self.players = players
        self.grid = Grid(rows, cols)
        self.solver = ConnectFourChecker(self.grid)
        self.winner = None
        self.is_over = False
        self.is_grid_full = False

    def next_player(self):
        self.current_player = (self.current_player + 1) % 2

    def get_current_player(self) -> str:
        return self.players[self.current_player]

    def insert_coin(self, col: int):
        color = self.get_current_player()
        row = self.grid.get_free_row(col)
        self.grid.insert(color, col)
        self.is_grid_full = self.grid.is_full()
        is_won = self.solver.check_win(color, row, col)
        if is_won or self.is_grid_full:
            self.is_over = True
            if is_won:
                self.winner = self.get_current_player()
        else:
            self.next_player()
