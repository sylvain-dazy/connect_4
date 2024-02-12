from src.console.view import View
from src.core.game import Game


class Controller:
    def __init__(self, game: Game, view: View):
        self.game = game
        self.view = view

    def play(self):
        running = True
        while running:
            self.view.display_game()
            user_action = input("> ")
            if user_action in {"quit", "exit", "end", "close"}:
                running = False
            elif self.game.winner is None:
                column = int(user_action)
                self.game.play(column - 1)
