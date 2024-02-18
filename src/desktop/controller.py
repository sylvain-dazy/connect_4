import pygame

from src.core.game import Game
from src.desktop.view import View


FPS = 50


class Controller:

    def __init__(self, game: Game, view: View):
        self.game = game
        self.view = view
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.handle(event)
            self.view.update()
            self.clock.tick(FPS)

    def handle(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.game.get_winner() is None:
            col = self.view.get_chosen_column()
            if self.game.grid.get_free_row(col) < 0:
                self.view.display_error_message("Column is full")
            else:
                self.view.animate_coin_chute()
                self.game.play(col)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            self.game.reset()
