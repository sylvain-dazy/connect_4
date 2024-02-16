import logging
import sys

from src.core.game import Game
from src.desktop.controller import Controller
from src.desktop.view import View

LOG_LEVEL = logging.INFO

if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL)
    game = Game("Red", "Yellow")
    Controller(game, View(game)).play()
    sys.exit()
