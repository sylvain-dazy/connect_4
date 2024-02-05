import logging
import sys

from src.console.controller import Controller
from src.console.view import View
from src.core.game import Game

ROWS = 6
COLS = 7
LOG_LEVEL = logging.INFO

if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL)
    game = Game(ROWS, COLS)
    Controller(game, View(game)).play()
    sys.exit()
