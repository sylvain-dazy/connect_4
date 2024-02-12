import pygame

from src.core.grid import Grid
from src.core.game import Game

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


class GridView:
    def __init__(self, grid: Grid):
        self.CELL_RADIUS = 40
        self.MARGIN = 10
        self.board_color = BLUE
        self.background_color = WHITE
        self.grid = grid
        self.CELL_SIZE = 2 * (self.CELL_RADIUS + self.MARGIN)
        width = self.grid.cols * self.CELL_SIZE
        height = self.grid.rows * self.CELL_SIZE
        self.surface = pygame.Surface((width, height))

    def update(self):
        self.surface.fill(self.board_color)
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                self.draw_coin(row, col)

    def draw_coin(self, row, col):
        color = self.get_color(self.grid.get_coin_color(row, col))
        center = self.get_coordinate(row, col)
        pygame.draw.circle(self.surface, color, center, self.CELL_RADIUS)

    def get_coordinate(self, row: int, col: int) -> tuple[int, int]:
        center_x = col * self.CELL_SIZE + self.CELL_SIZE // 2
        center_y = row * self.CELL_SIZE + self.CELL_SIZE // 2
        return center_x, center_y

    def get_color(self, coin: str) -> tuple[int, int, int]:
        if coin == "R":
            return RED
        if coin == "Y":
            return YELLOW
        return self.background_color


class View:
    def __init__(self, game: Game):
        self.CELL_RADIUS = 40
        self.CELL_MARGIN = 10
        self.COIN_RADIUS = 40
        self.BOARD_MARGIN = 10
        self.INSERTION_AREA_HEIGHT = 100
        self.board_color = BLUE
        self.background_color = WHITE
        self.game = game
        self.grid_view = GridView(self.game.grid)
        window_width = self.grid_view.surface.get_width() + 2 * self.BOARD_MARGIN
        window_height = self.grid_view.surface.get_height() + self.INSERTION_AREA_HEIGHT + self.BOARD_MARGIN
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.chosen_column = 0

    def update(self):
        self.screen.fill(self.background_color)
        self.draw_next_coin()
        self.grid_view.update()
        self.screen.blit(self.grid_view.surface, (self.BOARD_MARGIN, self.INSERTION_AREA_HEIGHT))
        pygame.display.update()

    def draw_next_coin(self):
        dist_between_2_center = 2 * (self.CELL_RADIUS + self.CELL_MARGIN)
        first_center = self.CELL_RADIUS + self.CELL_MARGIN + self.BOARD_MARGIN
        center = (self.chosen_column * dist_between_2_center + first_center, self.CELL_MARGIN + self.CELL_RADIUS)
        if self.game.get_current_player() == "R":
            color = RED
        else:
            color = YELLOW
        self.draw_coin(center, color)

    def draw_coin(self, center, color):
        pygame.draw.circle(self.screen, color, center, self.COIN_RADIUS)

    def compute_chosen_column(self, x: int) -> int:
        return (x - self.BOARD_MARGIN) // self.INSERTION_AREA_HEIGHT
