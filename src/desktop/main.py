import logging
import sys

from src.core.game import Game
from src.desktop.controller import Controller
from src.desktop.view import View

ROWS = 6
COLS = 7
LOG_LEVEL = logging.INFO

if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL)
    game = Game(ROWS, COLS)
    Controller(game, View(game)).play()
    sys.exit()
