import pygame

from src.core.game import Game
from src.core.grid import Grid

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

BACKGROUND_COLOR = WHITE
BOARD_COLOR = BLUE

BOARD_MARGIN = 10
CELL_MARGIN = 5
CELL_RADIUS = 40
CELL_SIZE = 2 * (CELL_RADIUS + CELL_MARGIN)
INSERTION_AREA_HEIGHT = 100


WINNER = {"en": "{} wins the game !",
          "fr": "{} a gagné la partie !"}


class GridView:
    def __init__(self, grid: Grid):
        self.grid = grid
        width = self.grid.cols * CELL_SIZE
        height = self.grid.rows * CELL_SIZE
        self.surface = pygame.Surface((width, height))

    def update(self):
        self.surface.fill(BOARD_COLOR)
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                self.draw_coin(row, col)

    def draw_coin(self, row, col):
        coin = self.grid.state[row][col]
        if coin == Grid.FREE:
            color = BACKGROUND_COLOR
        elif coin == 0:
            color = RED
        else:
            color = YELLOW
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(self.surface, color, (center_x, center_y), CELL_RADIUS)


class View:
    def __init__(self, game: Game):
        self.game = game
        self.grid_view = GridView(self.game.grid)
        window_width = self.grid_view.surface.get_width() + 2 * BOARD_MARGIN
        window_height = self.grid_view.surface.get_height() + INSERTION_AREA_HEIGHT + BOARD_MARGIN
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.chosen_column = 0
        pygame.font.init()
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 64)

    def update(self):
        self.screen.fill(BACKGROUND_COLOR)
        if self.game.get_winner() is None:
            self.draw_next_coin()
        else:
            rendered = self.font.render(WINNER["en"].format(self.game.get_winner()), True, BLACK)
            self.screen.blit(rendered, ((self.screen.get_width() - rendered.get_width()) // 2, (INSERTION_AREA_HEIGHT - rendered.get_height()) // 2))
        self.grid_view.update()
        self.screen.blit(self.grid_view.surface, (BOARD_MARGIN, INSERTION_AREA_HEIGHT))
        pygame.display.update()

    def draw_next_coin(self):
        chosen_column = self.get_chosen_column()
        dist_between_2_center = 2 * (CELL_RADIUS + CELL_MARGIN)
        first_center = CELL_RADIUS + CELL_MARGIN + BOARD_MARGIN
        center = (chosen_column * dist_between_2_center + first_center, CELL_MARGIN + CELL_RADIUS)
        if self.game.get_current_player() == "Sylvain":
            color = RED
        else:
            color = YELLOW
        self.draw_coin(center, color)

    def draw_coin(self, center, color):
        pygame.draw.circle(self.screen, color, center, CELL_RADIUS)

    def get_chosen_column(self) -> int:
        x, y = pygame.mouse.get_pos()
        return (x - BOARD_MARGIN) // INSERTION_AREA_HEIGHT
