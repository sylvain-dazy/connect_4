from src.core.game import Game


QUIT_ACTION = {"en": "q",
               "fr": "q"}
NEW_GAME_ACTION = {"en": "n",
                   "fr": "n"}
TURN = {"en": "It's {}'s turn",
        "fr": "C'est au tour de {}"}
MENU = {"en": "Enter the column number, {} to stat a new game or {} to exit the game",
        "fr": "Entrez le numéro de la colonne, {} pour commencer un nouveau jeu ou {} pour quitter le jeu"}
WINNER = {"en": "{} wins the game",
          "fr": "{} a gagné !"}


class View:

    def __init__(self, game: Game, lang: str):
        self.lang = lang
        self.game = game
        self.EMPTY_CELL_SYMBOL = " "
        self.CELL_SEPARATOR = "|"
        self.BOTTOM_SEPERATOR = "-"
        self.SYMBOLS = {game.players[0]: "X", game.players[1]: "O"}
        self.new_game_action = NEW_GAME_ACTION[lang]
        self.quit_action = QUIT_ACTION[lang]

    def display_game(self):
        self.display_grid()
        if self.game.get_winner() is not None:
            self.display_winner()
        else:
            self.display_turn()
        self.display_menu()

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

    def display_turn(self):
        print(TURN[self.lang].format(self.game.get_current_player()))

    def display_menu(self):
        print(MENU[self.lang].format(NEW_GAME_ACTION[self.lang], QUIT_ACTION[self.lang]))

    def get_symbol(self, row: int, col: int):
        coin = self.game.grid.state[row][col]
        if coin is self.game.grid.FREE:
            return self.EMPTY_CELL_SYMBOL
        return self.SYMBOLS[self.game.players[coin]]

    def display_winner(self):
        print(WINNER[self.lang].format(self.game.get_winner()))
