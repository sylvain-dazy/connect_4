import src.console.configuration as cfg

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
            user_action = input(cfg.USER_ACTION_INVITE_COMMAND.format(self.game.get_current_player()))
            if user_action == self.view.quit_action:
                running = False
            elif user_action == self.view.new_game_action:
                self.game.reset()
            elif self.game.winner is None:
                column = int(user_action)
                self.game.play(column - 1)
