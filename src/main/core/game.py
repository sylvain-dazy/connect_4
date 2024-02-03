from src.main.core.board import Board


class GameSolver:

    def __init__(self, board: Board):
        self.board = board

    def check_win(self, color: str, row: int, col: int) -> bool:
        if self.check_4_in_row(color, row, col):
            return True
        if self.check_4_in_col(color, row, col):
            return True
        if self.check_4_in_diagonally_down_left_up_right(color, row, col):
            return True
        if self.check_4_in_diagonally_down_right_up_left(color, row, col):
            return True
        return False

    def check_4_in_col(self, color: str, row: int, col: int) -> bool:
        count = 1
        i = 1
        while i < 4 and col + i < 7 and self.board.get_coin_color(row, col + i) == color:
            count += 1
            i += 1
        if count == 4:
            return True
        i = 1
        while i < 4 and col - i >= 0 and self.board.get_coin_color(row, col - i) == color:
            count += 1
            i += 1
        if count == 4:
            return True
        return False

    def check_4_in_row(self, color: str, row: int, col: int) -> bool:
        count = 1
        i = 1
        while i < 4 and row + i < 6 and self.board.get_coin_color(row + i, col) == color:
            count += 1
            i += 1
        if count == 4:
            return True
        i = 1
        while i < 4 and row - i >= 0 and self.board.get_coin_color(row - i, col) == color:
            count += 1
            i += 1
        if count == 4:
            return True
        return False

    def check_4_in_diagonally_down_left_up_right(self, color: str, row: int, col: int) -> bool:
        count = 1
        i = 1
        while i < 4 and row + i < 6 and col + i < 7 and self.board.get_coin_color(row + i, col + i) == color:
            count += 1
            i += 1
        if count == 4:
            return True
        i = 1
        while i < 4 and row - i >= 0 and col - i >= 0 and self.board.get_coin_color(row - i, col - i) == color:
            count += 1
            i += 1
        if count == 4:
            return True
        return False

    def check_4_in_diagonally_down_right_up_left(self, color: str, row: int, col: int) -> bool:
        count = 1
        i = 1
        while i < 4 and row - i >= 0 and col + i < 7 and self.board.get_coin_color(row - i, col + i) == color:
            count += 1
            i += 1
        if count == 4:
            return True
        i = 1
        while i < 4 and row + i < 6 and col - i >= 0 and self.board.get_coin_color(row + i, col - i) == color:
            count += 1
            i += 1
        if count == 4:
            return True
        return False


class Game:

    def __init__(self, rows: int = 6, cols: int = 7, colors: tuple[str, str] = ("R", "Y")):
        self.board = Board(rows, cols)
        self.solver = GameSolver(self.board)
        self.color = colors
        self.current_player = 0
        self.winner = None
        self.is_over = False
        self.is_grid_full = False

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.color)

    def get_current_color(self) -> str:
        return self.color[self.current_player]

    def insert_coin(self, col: int):
        color = self.get_current_color()
        row = self.board.get_free_row(col)
        self.board.insert_coin(color, col)
        self.is_grid_full = self.board.is_full()
        is_won = self.solver.check_win(color, row, col)
        if is_won or self.is_grid_full:
            self.is_over = True
            if is_won:
                self.winner = self.get_current_color()
        else:
            self.next_player()
