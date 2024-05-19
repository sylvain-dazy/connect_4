from src.core.grid import Grid


class ConnectFourChecker:

    def __init__(self, grid: Grid, count_to_win: int):
        self.grid = grid
        self.count_to_win = count_to_win

    def check(self):
        for r in range(self.grid.rows):
            w = self.connect_four_in_row(r)
            if w is not None:
                return w
        for c in range(self.grid.cols):
            w = self.connect_four_in_col(c)
            if w is not None:
                return w
        for r in range(self.grid.rows):
            w = self.connect_four_in_diagonal_bottom_left_to_top_right(r, 0)
            if w is not None:
                return w
        for c in range(self.grid.cols):
            w = self.connect_four_in_diagonal_bottom_left_to_top_right(self.grid.rows - 1, c)
            if w is not None:
                return w
        for r in range(self.grid.rows):
            w = self.connect_four_in_diagonal_top_left_to_bottom_right(r, 0)
            if w is not None:
                return w
        for c in range(self.grid.cols):
            w = self.connect_four_in_diagonal_top_left_to_bottom_right(0, c)
            if w is not None:
                return w
        return None

    def connect_four_in_row(self, row):
        current = self.grid.state[row][0]
        count = 1
        col = 1
        while col < self.grid.cols and count < self.count_to_win:
            c = self.grid.state[row][col]
            if c is not None and c == current:
                count += 1
            else:
                current = c
                count = 1
            col += 1
        if count == self.count_to_win:
            return current
        return None

    def connect_four_in_col(self, col):
        current = self.grid.state[0][col]
        count = 1
        row = 1
        while row < self.grid.rows and count < self.count_to_win:
            c = self.grid.state[row][col]
            if c is not None and c == current:
                count += 1
            else:
                current = c
                count = 1
            row += 1
        if count == self.count_to_win:
            return current
        return None

    def connect_four_in_diagonal_bottom_left_to_top_right(self, row, col):
        current = self.grid.state[row][col]
        count = 1
        i = 1
        while row - i >= 0 and col + i < self.grid.cols and count < self.count_to_win:
            c = self.grid.state[row - i][col + i]
            if c is not None and c == current:
                count += 1
            else:
                current = c
                count = 1
            i += 1
        if count == self.count_to_win:
            return current
        return None

    def connect_four_in_diagonal_top_left_to_bottom_right(self, row, col):
        current = self.grid.state[row][col]
        count = 1
        i = 1
        while row + i < self.grid.rows and col + i < self.grid.cols and count < self.count_to_win:
            c = self.grid.state[row + i][col + i]
            if c is not None and c == current:
                count += 1
            else:
                current = c
                count = 1
            i += 1
        if count == self.count_to_win:
            return current
        return None
