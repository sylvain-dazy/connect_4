import logging

import pygame.font

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
BLUE = (0, 0, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
YELLOW = (255, 255, 0, 255)
SKY_BLUE = (0, 255, 255, 255)
PINK = (255, 0, 255, 255)
TRANSPARENCY = (0, 0, 0, 0)

BACKGROUND_COLOR = WHITE
BOARD_COLOR = BLUE
FONT_COLOR = BLACK
EDGE_COLOR = BLACK

EDGE_WIDTH = 2
BOARD_MARGIN = 10
CELL_MARGIN = 5
COIN_RADIUS = 30
COINS_SPEED = 2

FONT = pygame.font.get_default_font()
FONT_SIZE = 48

WINNER = {"en": "{} wins the game !",
          "fr": "{} a gagné la partie !"}

DRAWN_GAME = {"en": "It's a draw !",
              "fr": "Match nul !"}

FPS = 50

LOG_LEVEL = logging.INFO

ROWS = 6
COLS = 7
COUNT_TO_WIN = 4

PLAYERS = [("Sylvain", RED), ("Julien", YELLOW)]
LANG = "fr"
