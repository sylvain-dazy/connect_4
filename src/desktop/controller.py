import logging

import pygame

from src.core.game import Game, ColumnFullError
from src.desktop.view import View

FPS = 50


class Controller:

    def __init__(self, game: Game, view: View):
        self.game = game
        self.view = view
        self.clock = pygame.time.Clock()
        self.running = False
        self.col = None

    def run(self):
        self.running = True
        self.view.update()
        while self.running:
            for event in pygame.event.get():
                self.handle(event)
            self.clock.tick(FPS)

    def handle(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            self.game.reset()
            self.col = self.view.get_chosen_column()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.game.get_winner() is None:
            try:
                self.view.animate_coin_chute(self.game.get_current_player())
                self.game.play(self.col)
            except ColumnFullError:
                logging.getLogger(Controller.__name__).error("Column is full")
        elif event.type == pygame.MOUSEMOTION and self.game.get_winner() is None:
            self.col = self.view.get_chosen_column()
            self.view.update()
