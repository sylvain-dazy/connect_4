from src.core.connect_four_checker import ConnectFourChecker
from src.core.grid import Grid

DEFAULT_ROWS = 6
DEFAULT_COLS = 7
DEFAULT_COUNT_TO_WIN = 4


class Game:
    def __init__(self, first, second, rows: int = DEFAULT_ROWS, cols: int = DEFAULT_COLS, count_to_win: int = DEFAULT_COUNT_TO_WIN):
        self.players = [first, second]
        self.current_player = 0
        self.grid = Grid(rows, cols)
        self.winner = None
        self.connect_four_checker = ConnectFourChecker(self.grid, count_to_win)

    def reset(self):
        self.winner = None
        self.current_player = 0
        self.grid.reset()

    def get_current_player(self):
        return self.players[self.current_player]

    def play(self, column: int):
        self.grid.insert(self.current_player, column)
        self.winner = self.connect_four_checker.check()
        self.current_player = self.next_player()

    def next_player(self) -> int:
        return (self.current_player + 1) % len(self.players)

    def get_winner(self):
        if self.winner is not None:
            return self.players[self.winner]
        return None


class ObservableGame(Game):
    def __init__(self, first, second, rows: int = DEFAULT_ROWS, cols: int = DEFAULT_COLS, count_to_win: int = DEFAULT_COUNT_TO_WIN):
        super().__init__(first, second, rows, cols, count_to_win)
        self.observers = []

    def add_observers(self, observer):
        self.observers.append(observer)

    def notify_all(self):
        for o in self.observers:
            o.update()

    def play(self, column: int):
        super().play(column)
        self.notify_all()

    def reset(self):
        super().reset()
        self.notify_all()
