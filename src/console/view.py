from src.core.game import Game


class View:
    def __init__(self, game: Game):
        self.game = game
        self.empty_cell = " "

    def display_game(self):
        for col in range(self.game.grid.cols):
            print(" " + str(col + 1), end="")
        print()
        for row in range(self.game.grid.rows):
            for col in range(self.game.grid.cols):
                symbol = self.get_symbol(row, col)
                print("|" + symbol, end="")
            print("|")
        print(self.game.grid.cols * "|-" + "|")

    def display_menu(self):
        if self.game.get_current_player() == "R":
            color = "red"
        else:
            color = "yellow"
        print("It's " + color + " player turn")

    @staticmethod
    def display_error(message: str):
        print("ERROR: " + message)

    def get_symbol(self, row: int, col: int):
        color = self.game.grid.get_coin_color(row, col)
        if color in ("R", "Y"):
            return color
        return self.empty_cell

    def display_winner(self):
        print(f"{self.game.winner} wins the game")
