class Game:
    def __init__(self, rows: int = 6, cols: int = 7, colors: tuple[str, str] = ("R", "Y")):
        self.grid = [["" for _ in range(cols)] for _ in range(rows)]
        self.color = colors
        self.current_player = 0

    def insert_coin(self, col: int):
        row = len(self.grid) - 1
        while row >= 0 and self.is_not_free(row, col):
            row -= 1
        if self.is_not_free(row, col):
            raise Game.ColumnIsFullError
        self.grid[row][col] = self.get_current_color()
        self.next_player()

    def is_not_free(self, row: int, col: int):
        return self.grid[row][col] != ""

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.color)

    def get_current_color(self) -> str:
        return self.color[self.current_player]

    class ColumnIsFullError(Exception):
        pass
