class Grid:

    FREE_SPACE = ""

    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.state = [[Grid.FREE_SPACE for _ in range(self.cols)] for _ in range(self.rows)]

    def insert_coin(self, coin: str, col: int):
        row = self.get_free_row(col)
        if row is None:
            raise Grid.ColumnIsFullError
        self.state[row][col] = coin

    def get_free_row(self, col: int) -> int | None:
        row = len(self.state) - 1
        while row >= 0:
            if self.is_free(row, col):
                return row
            row -= 1
        return None

    def is_column_full(self, col: int) -> bool:
        return not self.is_free(0, col)

    def is_free(self, row: int, col: int) -> bool:
        return self.state[row][col] == Grid.FREE_SPACE

    def is_full(self) -> bool:
        for row in range(6):
            for col in range(7):
                if self.is_free(row, col):
                    return False
        return True

    def get_coin_color(self, row: int, col: int) -> str:
        return self.state[row][col]

    class ColumnIsFullError(Exception):
        pass
