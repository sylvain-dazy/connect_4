import sys

import pygame

from src.main.core.game import Game

FPS = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROWS = 6
COLS = 7

BOARD_MARGIN_LEFT = 10
CELL_RADIUS = 40
CELL_MARGIN = 10

if __name__ == '__main__':
    game = Game(ROWS, COLS)
    game.insert_coin(0)
    game.insert_coin(0)
    game.insert_coin(0)
    pygame.init()
    screen = pygame.display.set_mode((COLS * 100 + 20, ROWS * 100 + 110))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, (10, 100, 100 * 7, 100 * 6))
        for row in range(6):
            for col in range(7):
                if game.grid[row][col] == "R":
                    color = RED
                elif game.grid[row][col] == "Y":
                    color = YELLOW
                else:
                    color = WHITE
                pygame.draw.circle(screen, color, (col * 2 * (CELL_RADIUS + CELL_MARGIN) + CELL_RADIUS + CELL_MARGIN + BOARD_MARGIN_LEFT, row * 2 * (CELL_RADIUS + CELL_MARGIN) + 3 * (CELL_RADIUS + CELL_MARGIN)), 40)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()
