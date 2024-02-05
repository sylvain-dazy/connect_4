from src.console.view import View
from src.core.board import Grid
from src.core.game import Game


class Controller:
    def __init__(self, game: Game, view: View):
        self.game = game
        self.view = view

    def play(self):
        running = True
        while running and not self.game.is_over:
            self.view.display_game()
            self.view.display_menu()
            user_action = input("> ")
            if user_action in {"quit", "exit", "end", "close"}:
                running = False
            else:
                column = int(user_action)
                if column <= 0 or column > self.game.grid.cols:
                    self.view.display_error("Invalid column value")
                else:
                    try:
                        self.game.insert_coin(column - 1)
                    except Grid.ColumnIsFullError:
                        self.view.display_error("Column " + str(column) + " is full")
        self.view.display_game()
        self.view.display_winner()
