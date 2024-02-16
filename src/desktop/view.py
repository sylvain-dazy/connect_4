import pygame

from src.core.game import Game
from src.core.grid import Grid

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

BACKGROUND_COLOR = (255, 255, 255, 0)
BOARD_COLOR = BLUE

BOARD_MARGIN = 10
CELL_MARGIN = 7
CELL_RADIUS = 40
CELL_SIZE = 2 * (CELL_RADIUS + CELL_MARGIN)
INSERTION_AREA_HEIGHT = 100

COINS_SPEED = 2

WINNER = {"en": "{} wins the game !",
          "fr": "{} a gagné la partie !"}


class GridView:
    def __init__(self, grid: Grid):
        self.cell_size = CELL_SIZE
        self.grid = grid
        width = self.grid.cols * CELL_SIZE
        height = self.grid.rows * CELL_SIZE
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

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
        x, y = self.get_coordinate_of(row, col)
        pygame.draw.circle(self.surface, color, (x, y), CELL_RADIUS)

    def get_coordinate_of(self, row: int, col: int) -> tuple[int, int]:
        center_x = col * self.cell_size + self.cell_size // 2
        center_y = row * self.cell_size + self.cell_size // 2
        return center_x, center_y

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
        self.speed = COINS_SPEED
        self.lang = "en"

    def update(self):
        self.screen.fill(BACKGROUND_COLOR)
        if self.game.get_winner() is None:
            self.draw_next_coin()
        else:
            rendered = self.font.render(WINNER[self.lang].format(self.game.get_winner()), True, BLACK)
            self.screen.blit(rendered, ((self.screen.get_width() - rendered.get_width()) // 2, (INSERTION_AREA_HEIGHT - rendered.get_height()) // 2))
        self.grid_view.update()
        self.screen.blit(self.grid_view.surface, (BOARD_MARGIN, INSERTION_AREA_HEIGHT))
        pygame.display.update()

    def draw_next_coin(self):
        center = self.get_center_of_next_coin()
        color = self.get_color()
        self.draw_coin(center, color)

    def get_center_of_next_coin(self):
        chosen_column = self.get_chosen_column()
        dist_between_2_center = 2 * (CELL_RADIUS + CELL_MARGIN)
        first_center = CELL_RADIUS + CELL_MARGIN + BOARD_MARGIN
        return chosen_column * dist_between_2_center + first_center, CELL_MARGIN + CELL_RADIUS

    def get_coordinate_of(self, row, col):
        x, y = self.grid_view.get_coordinate_of(row, col)
        return x + BOARD_MARGIN, y + INSERTION_AREA_HEIGHT

    def get_color(self):
        if self.game.current_player == 0:
            return RED
        return YELLOW

    def draw_coin(self, center, color):
        pygame.draw.circle(self.screen, color, center, CELL_RADIUS)

    def get_chosen_column(self) -> int:
        x, y = pygame.mouse.get_pos()
        if x < BOARD_MARGIN:
            return 0
        return (x - BOARD_MARGIN) // CELL_SIZE

    def animate_coin_chute(self):
        color = self.get_color()
        x, y = self.get_center_of_next_coin()
        col = self.get_chosen_column()
        row = self.game.grid.get_free_row(col)
        x_f, y_f = self.get_coordinate_of(row, col)
        while y < y_f:
            self.screen.fill(BACKGROUND_COLOR)
            self.draw_coin((x, y), color)
            self.grid_view.update()
            self.screen.blit(self.grid_view.surface, (BOARD_MARGIN, INSERTION_AREA_HEIGHT))
            pygame.display.update()
            y += self.speed
