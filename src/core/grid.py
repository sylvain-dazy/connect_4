class Grid:
    def __init__(self, rows: int, columns: int, initial_state: list[list] = None):
        self.rows = rows
        self.cols = columns
        self.inserted_coins = 0
        if initial_state is None:
            self.state = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.state = initial_state

    def insert(self, coin, column: int):
        free_row = self.get_free_row(column)
        self.state[free_row][column] = coin
        self.inserted_coins += 1

    def get_free_row(self, column: int) -> int:
        free_row = self.rows - 1
        while free_row >= 0 and self.state[free_row][column] is not None:
            free_row -= 1
        return free_row

    def __is_valid(self, column: int) -> bool:
        return 0 <= column < self.cols

    def reset(self):
        self.state = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.inserted_coins = 0

    def is_full(self):
        return self.inserted_coins == self.rows * self.cols
