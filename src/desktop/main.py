import logging
import sys

import pygame

from src.core.game import Game
from src.desktop.controller import Controller
from src.desktop.view import View

LOG_LEVEL = logging.INFO

if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL)
    game = Game("Red", "Yellow")
    pygame.init()
    pygame.font.init()
    Controller(game, View(game)).run()
    pygame.quit()
    sys.exit()
