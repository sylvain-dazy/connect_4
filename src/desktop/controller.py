import logging

import pygame

from src.core.game import Game
from src.desktop.view import View


class Controller:

    def __init__(self, game: Game, view: View):
        self.FPS = 50
        pygame.init()
        self.game = game
        self.view = view
        self.clock = pygame.time.Clock()
        self.chosen_column = 0

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.chosen_column = self.view.compute_chosen_column(event.pos[0])
                    self.view.chosen_column = self.chosen_column
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.insert_coin(self.chosen_column)
            self.view.update()
            if self.game.is_over:
                self.display_winner()
                self.pause_the_game()
                running = False
        self.clock.tick(self.FPS)
        pygame.quit()

    def display_winner(self):
        logging.getLogger(View.__name__).info("Game over")
        if self.game.winner is not None:
            logging.getLogger(View.__name__).info("Winner is " + self.game.winner + " player")
        else:
            logging.getLogger(View.__name__).info("It's a draw")

    def pause_the_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.clock.tick(self.FPS)

    def insert_coin(self, col: int):
        if self.game.grid.is_column_full(col):
            logging.getLogger(View.__name__).error("Error: Column is full")
        else:
            self.game.insert_coin(col)
