import logging
import sys

import pygame

import src.desktop.configuration as cfg

from src.core.game import ObservableGame
from src.desktop.controller import Controller
from src.desktop.view import View


if __name__ == '__main__':
    logging.basicConfig(level=cfg.LOG_LEVEL)
    pygame.init()
    pygame.font.init()
    game = ObservableGame(cfg.PLAYERS)
    view = View(game, cfg.LANG)
    game.add_observers(view)
    Controller(game, view).run()
    pygame.quit()
    sys.exit()
