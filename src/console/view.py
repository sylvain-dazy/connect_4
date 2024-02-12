from src.core.game import Game


TURN = {"en": "It's {}'s turn"}
ACTIONS = {"en": "Enter the column number or quit, exit or close"}
ERROR_PREFIX = {"en": "ERROR: "}
WINNER = {"en": "{} wins the game"}


class View:

    def __init__(self, game: Game, lang: str):
        self.lang = lang
        self.game = game
        self.EMPTY_CELL_SYMBOL = " "
        self.CELL_SEPARATOR = "|"
        self.BOTTOM_SEPERATOR = "-"
        self.SYMBOLS = {game.players[0]: "R", game.players[1]: "Y"}

    def display_game(self):
        self.display_grid()
        self.display_menu()
        if self.game.winner is not None:
            self.display_winner()

    def display_grid(self):
        self.display_grid_header()
        self.display_rows_and_cols()
        self.display_bottom_line()

    def display_grid_header(self):
        for col in range(self.game.grid.cols):
            print(" " + str(col + 1), end="")
        print()

    def display_rows_and_cols(self):
        for row in range(self.game.grid.rows):
            self.display_one_row(row)

    def display_one_row(self, row: int):
        for col in range(self.game.grid.cols):
            symbol = self.get_symbol(row, col)
            print(self.CELL_SEPARATOR + symbol, end="")
        print(self.CELL_SEPARATOR)

    def display_bottom_line(self):
        print(self.game.grid.cols * (self.CELL_SEPARATOR + self.BOTTOM_SEPERATOR) + self.CELL_SEPARATOR)

    def display_menu(self):
        print(TURN[self.lang].format(self.game.get_current_player()))
        print(ACTIONS[self.lang])

    def display_error(self, message: str):
        print(ERROR_PREFIX[self.lang] + message)

    def get_symbol(self, row: int, col: int):
        coin = self.game.grid.state[row][col]
        if coin is self.game.grid.FREE:
            return self.EMPTY_CELL_SYMBOL
        return self.SYMBOLS[self.game.players[coin]]

    def display_winner(self):
        print(WINNER[self.lang].format(self.game.get_winner()))
