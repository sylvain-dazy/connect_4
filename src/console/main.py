import logging
import sys

import src.console.configuration as cfg

from src.console.controller import Controller
from src.console.view import View
from src.core.game import Game


if __name__ == '__main__':
    logging.basicConfig(level=cfg.LOG_LEVEL)
    game = Game(cfg.PLAYERS[0][0], cfg.PLAYERS[1][0], cfg.ROWS, cfg.COLS, cfg.COUNT_TO_WIN)
    Controller(game, View(game, cfg.LANG)).play()
    sys.exit()
