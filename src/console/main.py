import logging
import sys

from src.console.controller import Controller
from src.console.view import View
from src.core.game import Game

LOG_LEVEL = logging.INFO
LANG = "fr"

if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL)
    game = Game("Sylvain", "Julien")
    Controller(game, View(game, LANG)).play()
    sys.exit()
