class Grid:

    FREE = None

    def __init__(self, rows: int = 6, columns: int = 7, initial_state: list[list] = None):
        if initial_state is None:
            self.rows = rows
            self.cols = columns
            self.state = [[Grid.FREE for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.rows = len(initial_state)
            self.cols = len(initial_state[0])
            self.state = initial_state

    def insert(self, coin: object, column: int):
        if not self.__is_valid(column):
            raise Grid.InvalidColumnError
        free_row = self.get_free_row(column)
        if free_row < 0:
            raise Grid.ColumnFullError
        self.state[free_row][column] = coin

    def get_free_row(self, column: int):
        free_row = self.rows - 1
        while free_row >= 0 and self.state[free_row][column] is not Grid.FREE:
            free_row -= 1
        return free_row

    def __is_valid(self, column: int) -> bool:
        return 0 <= column < self.cols

    class ColumnFullError(Exception):
        pass

    class InvalidColumnError(Exception):
        pass
