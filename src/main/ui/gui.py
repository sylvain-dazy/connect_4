import logging

import pygame

from src.main.core.game import Game


class GameView:
    def __init__(self, game: Game):
        self.FPS = 50
        self.color = {"white": (255, 255, 255),
                      "black": (0, 0, 0),
                      "blue": (0, 0, 255),
                      "red": (255, 0, 0),
                      "yellow": (255, 255, 0)}
        self.BOARD_MARGIN_LEFT = 10
        self.CELL_RADIUS = 40
        self.CELL_MARGIN = 10
        self.game = game
        self.board_color = self.color["blue"]
        self.background_color = self.color["white"]
        self.ROWS = len(self.game.grid)
        self.COLS = len(self.game.grid[0])
        self.cell_size = 2 * (self.CELL_RADIUS + self.CELL_MARGIN)
        window_width = self.COLS * self.cell_size + 2 * self.CELL_MARGIN
        window_height = (self.ROWS + 1) * self.cell_size + 2 * self.CELL_MARGIN
        pygame.init()
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.chosen_column = 0

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    pos = event.pos[0]
                    self.chosen_column = (pos - self.BOARD_MARGIN_LEFT) // self.cell_size
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    try:
                        self.game.insert_coin(self.chosen_column)
                    except Game.ColumnIsFullError:
                        logging.getLogger(GameView.__name__).error("Error: Column is full")
            self.draw_game()
            self.clock.tick(self.FPS)
        pygame.quit()

    def draw_game(self):
        self.screen.fill(self.background_color)
        self.draw_next_coin()
        self.draw_board(self.BOARD_MARGIN_LEFT, self.cell_size)
        pygame.display.update()

    def draw_next_coin(self):
        dist_between_2_center = 2 * (self.CELL_RADIUS + self.CELL_MARGIN)
        first_center = self.CELL_RADIUS + self.CELL_MARGIN + self.BOARD_MARGIN_LEFT
        center = (self.chosen_column * dist_between_2_center + first_center, self.CELL_MARGIN + self.CELL_RADIUS)
        if self.game.get_current_color() == "R":
            color = self.color["red"]
        else:
            color = self.color["yellow"]
        pygame.draw.circle(self.screen, color, center, self.CELL_RADIUS)

    def draw_board(self, margin_left: int, margin_top: int):
        dist_between_2_center = 2 * (self.CELL_RADIUS + self.CELL_MARGIN)
        first_center = (self.CELL_RADIUS + self.CELL_MARGIN + margin_left, 3 * (self.CELL_RADIUS + self.CELL_MARGIN))
        pygame.draw.rect(self.screen, self.color["blue"], (margin_left, margin_top, self.cell_size * self.COLS, self.cell_size * self.ROWS))
        for row in range(6):
            for col in range(7):
                if self.game.grid[row][col] == "R":
                    color = self.color["red"]
                elif self.game.grid[row][col] == "Y":
                    color = self.color["yellow"]
                else:
                    color = self.background_color
                center = (col * dist_between_2_center + first_center[0], row * dist_between_2_center + first_center[1])
                pygame.draw.circle(self.screen, color, center, self.CELL_RADIUS)
