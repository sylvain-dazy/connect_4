DEFAULT_NB_ROWS = 6
DEFAULT_NB_COLS = 7
DEFAULT_COUNT_TO_WIN = 4


class InvalidColumnError(RuntimeError):
    pass


class ColumnFullError(RuntimeError):
    pass


class Game:
    def __init__(self,
                 players: list[str],
                 rows: int = DEFAULT_NB_ROWS,
                 cols: int = DEFAULT_NB_COLS,
                 count_to_win: int = DEFAULT_COUNT_TO_WIN):
        self.players = players
        self.number_of_rows = rows
        self.number_of_cols = cols
        self.count_to_win = count_to_win
        self.current_player = 0
        self.winner = None
        self.inserted_coins = 0
        self.grid = self.__new_empty_grid()
        self.last_inserted = None

    def rows(self) -> int:
        return self.number_of_rows

    def cols(self) -> int:
        return self.number_of_cols

    def get_winner(self) -> str | None:
        return self.winner

    def get_coin_at(self, row: int, col: int):
        return self.grid[row][col]

    def reset(self):
        self.winner = None
        self.current_player = 0
        self.grid = self.__new_empty_grid()
        self.inserted_coins = 0

    def get_current_player(self) -> str:
        return self.players[self.current_player]

    def play(self, column: int):
        if self.is_over():
            return
        if not self.__is_column_valid(column):
            raise InvalidColumnError
        if self.__is_column_full(column):
            raise ColumnFullError
        free_row = self.__get_free_row(column)
        coin = self.get_current_player()
        self.grid[free_row][column] = coin
        self.last_inserted = (free_row, column)
        self.inserted_coins += 1
        self.winner = self.check()
        self.current_player = self.__next_player()

    def __next_player(self) -> int:
        return (self.current_player + 1) % len(self.players)

    def __new_empty_grid(self) -> list[list[None | str]]:
        return [[None for _ in range(self.cols())] for _ in range(self.rows())]

    def __is_column_valid(self, column: int) -> bool:
        return 0 <= column < self.cols()

    def __is_column_full(self, column: int) -> bool:
        return self.get_coin_at(0, column) is not None

    def is_over(self) -> bool:
        return self.get_winner() is not None or self.__is_full()

    def __get_free_row(self, column: int) -> int:
        free_row = self.rows() - 1
        while free_row >= 0 and self.grid[free_row][column] is not None:
            free_row -= 1
        return free_row

    def __is_full(self):
        return self.inserted_coins == self.rows() * self.cols()

    def check(self) -> str | None:
        for r in range(self.rows()):
            w = self.__connect_four_in_row(r)
            if w is not None:
                return w
        for c in range(self.cols()):
            w = self.__connect_four_in_col(c)
            if w is not None:
                return w
        for r in range(self.rows()):
            w = self.__connect_four_in_diagonal_bottom_left_to_top_right(r, 0)
            if w is not None:
                return w
        for c in range(self.cols()):
            w = self.__connect_four_in_diagonal_bottom_left_to_top_right(self.rows() - 1, c)
            if w is not None:
                return w
        for r in range(self.rows()):
            w = self.__connect_four_in_diagonal_top_left_to_bottom_right(r, 0)
            if w is not None:
                return w
        for c in range(self.cols()):
            w = self.__connect_four_in_diagonal_top_left_to_bottom_right(0, c)
            if w is not None:
                return w
        return None

    def __connect_four_in_row(self, row: int) -> str | None:
        current = self.get_coin_at(row, 0)
        count = 1
        col = 1
        while col < self.cols() and count < self.count_to_win:
            c = self.get_coin_at(row, col)
            if c is not None and c == current:
                count += 1
            else:
                current = c
                count = 1
            col += 1
        if count == self.count_to_win:
            return current
        return None

    def __connect_four_in_col(self, col: int) -> str | None:
        current = self.get_coin_at(0, col)
        count = 1
        row = 1
        while row < self.rows() and count < self.count_to_win:
            c = self.get_coin_at(row, col)
            if c is not None and c == current:
                count += 1
            else:
                current = c
                count = 1
            row += 1
        if count == self.count_to_win:
            return current
        return None

    def __connect_four_in_diagonal_bottom_left_to_top_right(self, row: int, col: int) -> str | None:
        current = self.get_coin_at(row, col)
        count = 1
        i = 1
        while row - i >= 0 and col + i < self.cols() and count < self.count_to_win:
            c = self.get_coin_at(row - i, col + i)
            if c is not None and c == current:
                count += 1
            else:
                current = c
                count = 1
            i += 1
        if count == self.count_to_win:
            return current
        return None

    def __connect_four_in_diagonal_top_left_to_bottom_right(self, row: int, col: int) -> str | None:
        current = self.get_coin_at(row, col)
        count = 1
        i = 1
        while row + i < self.rows() and col + i < self.cols() and count < self.count_to_win:
            c = self.get_coin_at(row + i, col + i)
            if c is not None and c == current:
                count += 1
            else:
                current = c
                count = 1
            i += 1
        if count == self.count_to_win:
            return current
        return None

    def get_coordinate_of_last_inserted(self):
        return self.last_inserted


class ObservableGame(Game):
    def __init__(self, players: list[str], rows: int = DEFAULT_NB_ROWS, cols: int = DEFAULT_NB_COLS, count_to_win: int = DEFAULT_COUNT_TO_WIN):
        super().__init__(players, rows, cols, count_to_win)
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
