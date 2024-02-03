class Board:

    FREE_SPACE = ""

    def __init__(self, rows: int = 6, cols: int = 7):
        self.grid = [[Board.FREE_SPACE for _ in range(cols)] for _ in range(rows)]

    def insert_coin(self, color: str, col: int):
        row = self.get_free_row(col)
        if row is None:
            raise Board.ColumnIsFullError
        self.grid[row][col] = color

    def get_free_row(self, col: int) -> int | None:
        row = len(self.grid) - 1
        while row >= 0:
            if self.is_free(row, col):
                return row
            row -= 1
        return None

    def is_not_free(self, row: int, col: int) -> bool:
        return not self.is_free(row, col)

    def is_free(self, row: int, col: int) -> bool:
        return self.grid[row][col] == Board.FREE_SPACE

    def is_full(self) -> bool:
        for row in range(6):
            for col in range(7):
                if self.is_free(row, col):
                    return False
        return True

    def get_coin_color(self, row: int, col: int) -> str:
        return self.grid[row][col]

    class ColumnIsFullError(Exception):
        pass
