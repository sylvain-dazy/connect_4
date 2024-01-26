import sys

import pygame

FPS = 50
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()
