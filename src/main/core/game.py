class Game:
    def __init__(self, rows: int = 6, cols: int = 7, colors: tuple[str, str] = ("R", "Y")):
        self.grid = [["" for _ in range(cols)] for _ in range(rows)]
        self.color = colors
        self.current_player = 0
        self.winner = None
        self.is_over = False
        self.is_grid_full = False

    def insert_coin(self, col: int):
        row = len(self.grid) - 1
        while row >= 0 and self.is_not_free(row, col):
            row -= 1
        if self.is_not_free(row, col):
            raise Game.ColumnIsFullError
        self.grid[row][col] = self.get_current_color()
        self.is_grid_full = self.is_full()
        is_won = self.check_win(row, col)
        if is_won or self.is_grid_full:
            self.is_over = True
            if is_won:
                self.winner = self.get_current_color()
        else:
            self.next_player()

    def is_not_free(self, row: int, col: int):
        return not self.is_free(row, col)

    def is_free(self, row: int, col: int):
        return self.grid[row][col] == ""

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.color)

    def get_current_color(self) -> str:
        return self.color[self.current_player]

    def is_full(self) -> bool:
        for row in range(6):
            for col in range(7):
                if self.is_free(row, col):
                    return False
        return True

    def check_win(self, row: int, col: int) -> bool:
        if self.check_4_in_row(row, col):
            return True
        if self.check_4_in_col(row, col):
            return True
        if self.check_4_in_diagonally_down_left_up_right(row, col):
            return True
        if self.check_4_in_diagonally_down_right_up_left(row, col):
            return True
        return False

    def check_4_in_col(self, row: int, col: int) -> bool:
        color = self.grid[row][col]
        count = 1
        i = 1
        while i < 4 and col + i < 7 and self.grid[row][col + i] == color:
            count += 1
            i += 1
        if count == 4:
            return True
        i = 1
        while i < 4 and col - i >= 0 and self.grid[row][col - i] == color:
            count += 1
            i += 1
        if count == 4:
            return True
        return False

    def check_4_in_row(self, row: int, col: int) -> bool:
        color = self.grid[row][col]
        count = 1
        i = 1
        while i < 4 and row + i < 6 and self.grid[row + i][col] == color:
            count += 1
            i += 1
        if count == 4:
            return True
        i = 1
        while i < 4 and row - i >= 0 and self.grid[row - i][col] == color:
            count += 1
            i += 1
        if count == 4:
            return True
        return False

    def check_4_in_diagonally_down_left_up_right(self, row: int, col: int) -> bool:
        color = self.grid[row][col]
        count = 1
        i = 1
        while i < 4 and row + i < 6 and col + i < 7 and self.grid[row + i][col + i] == color:
            count += 1
            i += 1
        if count == 4:
            return True
        i = 1
        while i < 4 and row - i >= 0 and col - i >= 0 and self.grid[row - i][col - i] == color:
            count += 1
            i += 1
        if count == 4:
            return True
        return False

    def check_4_in_diagonally_down_right_up_left(self, row: int, col: int) -> bool:
        color = self.grid[row][col]
        count = 1
        i = 1
        while i < 4 and row - i >= 0 and col + i < 7 and self.grid[row - i][col + i] == color:
            count += 1
            i += 1
        if count == 4:
            return True
        i = 1
        while i < 4 and row + i < 6 and col - i >= 0 and self.grid[row + i][col - i] == color:
            count += 1
            i += 1
        if count == 4:
            return True
        return False

    class ColumnIsFullError(Exception):
        pass
