import pygame

from src.core.game import Game
from src.desktop.view import View


FPS = 50


class Controller:

    def __init__(self, game: Game, view: View):
        pygame.init()
        self.game = game
        self.view = view
        self.clock = pygame.time.Clock()

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.game.get_winner() is None:
                    self.game.play(self.view.get_chosen_column())
            self.view.update()
        self.clock.tick(FPS)
        pygame.quit()
