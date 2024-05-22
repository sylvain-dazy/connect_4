import pygame

import src.desktop.configuration as cfg

from src.core.game import Game

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
BLUE = (0, 0, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
YELLOW = (255, 255, 0, 255)
SKY_BLUE = (0, 255, 255, 255)
PINK = (255, 0, 255, 255)
TRANSPARENCY = (0, 0, 0, 0)

BACKGROUND_COLOR = WHITE
BOARD_COLOR = BLUE
FONT_COLOR = BLACK
EDGE_COLOR = BLACK
PLAYERS_COLORS = [RED, YELLOW]

EDGE_WIDTH = 2
BOARD_MARGIN = 10
CELL_MARGIN = 5
COIN_RADIUS = 40
COINS_SPEED = 2

FONT = pygame.font.get_default_font()
FONT_SIZE = 64

WINNER_TXT = {"en": "{} wins the game !",
              "fr": "{} a gagné la partie !"}
DRAWN_TXT = {"en": "It's a draw !",
             "fr": "Match nul !"}


def get_cell_size(coin_radius, cell_margin) -> int:
    return 2 * (coin_radius + cell_margin)


CELL_SIZE = get_cell_size(COIN_RADIUS, CELL_MARGIN)


def get_coordinate_of(row: int, col: int, cell_size: int) -> tuple[int, int]:
    center_x = col * cell_size + cell_size // 2
    center_y = row * cell_size + cell_size // 2
    return center_x, center_y


def get_grid_size(game: Game, cell_size):
    width = game.cols() * cell_size
    height = game.rows() * cell_size
    return width, height


class Player:
    def __init__(self, name: str, coin):
        self.name = name
        self.coin = coin


class GridPresenter:
    def __init__(self, game: Game):
        self.game = game
        self.width, self.height = get_grid_size(game, CELL_SIZE)
        self.players = {Player(cfg.PLAYERS[0], PLAYERS_COLORS[0]),
                        Player(cfg.PLAYERS[1], PLAYERS_COLORS[1])}

    def draw_grid(self, game):
        for row in range(game.rows()):
            for col in range(game.cols()):
                self.draw_coin(game.get_coin_at(row, col), row, col)

    def get_color(self, player):
        for p in self.players:
            if player == p.name:
                return p.coin
        return self.get_no_coin_value()

    def get_no_coin_value(self):
        raise NotImplementedError

    def draw_coin(self, player, row, col):
        pass


def draw_coin(surface: pygame.Surface, color, center: tuple[int, int]):
    pygame.draw.circle(surface, color, center, COIN_RADIUS)
    pygame.draw.circle(surface, EDGE_COLOR, center, COIN_RADIUS, width=EDGE_WIDTH)


class GridView(GridPresenter):
    def __init__(self, game: Game):
        super().__init__(game)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

    def update(self):
        self.surface.fill(BOARD_COLOR)
        super().draw_grid(self.game)
        pygame.draw.rect(self.surface, EDGE_COLOR, self.surface.get_rect(), width=EDGE_WIDTH)

    def draw_coin(self, player, row, col):
        color = self.get_color(self.game.get_coin_at(row, col))
        x, y = get_coordinate_of(row, col, CELL_SIZE)
        draw_coin(self.surface, color, (x, y))

    def get_no_coin_value(self):
        return TRANSPARENCY

    def get_size(self):
        return self.surface.get_width(), self.surface.get_height()


def get_window_size(grid_size: tuple[int, int], margin: int, insertion_area_height: int):
    window_width = grid_size[0] + 2 * margin
    window_height = grid_size[1] + insertion_area_height + 2 * margin
    return window_width, window_height


class View:
    def __init__(self, game: Game, lang: str):
        self.game = game
        self.lang = lang
        self.grid = GridView(self.game)
        self.margin = BOARD_MARGIN
        self.cell_size = CELL_SIZE
        self.insertion_area_height = get_cell_size(COIN_RADIUS, self.margin)
        self.screen = pygame.display.set_mode(get_window_size(self.grid.get_size(), self.margin, self.insertion_area_height))
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)
        self.chosen_column = 0

    def update(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_insertion_area()
        self.draw_grid()
        pygame.display.update()

    def draw_insertion_area(self):
        if not self.game.is_over():
            self.draw_next_coin()
        elif self.game.is_over() and self.game.get_winner() is None:
            self.draw_drawn_game(DRAWN_TXT[self.lang])
        else:
            self.draw_winner(WINNER_TXT[self.lang].format(self.game.get_winner()))

    def draw_grid(self):
        self.grid.update()
        self.screen.blit(self.grid.surface, (self.margin, self.insertion_area_height))

    def get_winner_txt_position(self, rendered_text):
        x = (self.screen.get_width() - rendered_text.get_width()) // 2
        y = (self.insertion_area_height - rendered_text.get_height()) // 2
        return x, y

    def draw_winner(self, winner: str):
        rendered = self.font.render(winner, True, FONT_COLOR)
        self.screen.blit(rendered, self.get_winner_txt_position(rendered))

    def draw_drawn_game(self, txt: str):
        rendered = self.font.render(txt, True, FONT_COLOR)
        self.screen.blit(rendered, self.get_winner_txt_position(rendered))

    def draw_next_coin(self):
        center = self.get_center_of_next_coin()
        color = self.get_color(self.game.get_current_player())
        draw_coin(self.screen, color, center)

    def get_center_of_next_coin(self):
        chosen_column = self.get_chosen_column()
        dist_between_2_center = 2 * (COIN_RADIUS + CELL_MARGIN)
        first_center = COIN_RADIUS + CELL_MARGIN + self.margin
        return chosen_column * dist_between_2_center + first_center, CELL_MARGIN + COIN_RADIUS

    def get_coordinate_of(self, row, col):
        x, y = get_coordinate_of(row, col, self.cell_size)
        return x + self.margin, y + self.insertion_area_height

    def get_color(self, player: str):
        if player == cfg.PLAYERS[0]:
            return PLAYERS_COLORS[0]
        return PLAYERS_COLORS[1]

    def get_chosen_column(self) -> int:
        x, y = pygame.mouse.get_pos()
        if x < self.margin:
            return 0
        if x >= self.margin + self.grid.get_size()[0]:
            return self.game.cols() - 1
        return (x - self.margin) // self.cell_size

    def get_row_of_last_inserted_coin(self, col):
        row = 0
        while row < self.game.rows() and self.game.get_coin_at(row, col) is None:
            row += 1
        return row - 1

    def animate_coin_chute(self, player):
        color = self.get_color(player)
        x, y = self.get_center_of_next_coin()
        col = self.get_chosen_column()
        row = self.get_row_of_last_inserted_coin(col)
        if row >= 0:
            x_f, y_f = self.get_coordinate_of(row, col)
            while y <= y_f:
                self.screen.fill(BACKGROUND_COLOR)
                draw_coin(self.screen, color, (x, y))
                self.draw_grid()
                pygame.display.update()
                y += COINS_SPEED
