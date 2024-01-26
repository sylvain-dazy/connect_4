import sys

from src.main.core.game import Game
from src.main.ui.console import Console
from src.main.ui.gui import GameView

ROWS = 6
COLS = 7

if __name__ == '__main__':
    game = Game(ROWS, COLS)
    Console(game).play()
    # GameView(game).play()
    sys.exit()
