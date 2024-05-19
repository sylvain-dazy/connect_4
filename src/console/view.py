import src.console.configuration as cfg

from src.core.game import Game


class View:

    def __init__(self, game: Game, lang: str):
        self.lang = lang
        self.game = game
        self.EMPTY_CELL_SYMBOL = cfg.EMPTY_CELL_SYMBOL
        self.CELL_SEPARATOR = cfg.CELL_SEPARATOR
        self.BOTTOM_SEPERATOR = cfg.BOTTOM_SEPARATOR
        self.SYMBOLS = {cfg.PLAYERS[i][0]: cfg.PLAYERS[i][1] for i in range(len(cfg.PLAYERS))}
        self.new_game_action = cfg.NEW_GAME_ACTION[lang]
        self.quit_action = cfg.QUIT_ACTION[lang]

    def display_game(self):
        self.display_grid()
        if self.game.get_winner() is not None:
            self.display_winner()
        self.display_menu()

    def display_grid(self):
        self.display_grid_header()
        self.display_rows_and_cols()
        self.display_bottom_line()

    def display_grid_header(self):
        for col in range(self.game.cols()):
            print(f" {str(col + 1)}", end="")
        print()

    def display_rows_and_cols(self):
        for row in range(self.game.rows()):
            self.display_one_row(row)

    def display_one_row(self, row: int):
        for col in range(self.game.cols()):
            symbol = self.get_symbol(row, col)
            print(self.CELL_SEPARATOR + symbol, end="")
        print(self.CELL_SEPARATOR)

    def display_bottom_line(self):
        print(self.game.cols() * (self.CELL_SEPARATOR + self.BOTTOM_SEPERATOR) + self.CELL_SEPARATOR)

    def display_menu(self):
        print(cfg.MENU[self.lang].format(cfg.NEW_GAME_ACTION[self.lang], cfg.QUIT_ACTION[self.lang]))

    def get_symbol(self, row: int, col: int):
        coin = self.game.get_coin_at(row, col)
        if coin is None:
            return self.EMPTY_CELL_SYMBOL
        return self.SYMBOLS[coin]

    def display_winner(self):
        print(cfg.WINNER[self.lang].format(self.game.get_winner()))
