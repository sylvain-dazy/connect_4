from src.core.board import Grid


class WinChecker:

    def __init__(self, board: Grid):
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
