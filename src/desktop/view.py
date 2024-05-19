import logging

import pygame

import src.desktop.configuration as cfg

from src.core.game import Game


def draw_coin(surface, color, center):
    pygame.draw.circle(surface, color, center, cfg.COIN_RADIUS)
    pygame.draw.circle(surface, cfg.EDGE_COLOR, center, cfg.COIN_RADIUS, width=cfg.EDGE_WIDTH)


class GridView:
    def __init__(self, game: Game):
        self.cell_size = 2 * (cfg.COIN_RADIUS + cfg.CELL_MARGIN)
        self.cell_size = self.cell_size
        self.game = game
        width = self.game.cols() * self.cell_size
        height = self.game.rows() * self.cell_size
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def update(self):
        self.surface.fill(cfg.BOARD_COLOR)
        for row in range(self.game.rows()):
            for col in range(self.game.cols()):
                self.draw_coin(row, col)
        pygame.draw.rect(self.surface, cfg.EDGE_COLOR, self.surface.get_rect(), width=cfg.EDGE_WIDTH)

    def draw_coin(self, row, col):
        coin = self.game.get_coin_at(row, col)
        if coin is None:
            color = cfg.TRANSPARENCY
        elif coin == cfg.PLAYERS[0][0]:
            color = cfg.PLAYERS[0][1]
        else:
            color = cfg.PLAYERS[1][1]
        x, y = self.get_coordinate_of(row, col)
        draw_coin(self.surface, color, (x, y))

    def get_coordinate_of(self, row: int, col: int) -> tuple[int, int]:
        center_x = col * self.cell_size + self.cell_size // 2
        center_y = row * self.cell_size + self.cell_size // 2
        return center_x, center_y


class View:
    def __init__(self, game: Game, lang: str = cfg.LANG):
        self.game = game
        self.grid_view = GridView(self.game)
        self.insertion_area_height = 2 * (cfg.COIN_RADIUS + cfg.BOARD_MARGIN)
        window_width = self.grid_view.surface.get_width() + 2 * cfg.BOARD_MARGIN
        window_height = self.grid_view.surface.get_height() + self.insertion_area_height + cfg.BOARD_MARGIN
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.chosen_column = 0
        self.font = pygame.font.SysFont(cfg.FONT, cfg.FONT_SIZE)
        self.speed = cfg.COINS_SPEED
        self.lang = lang

    def update(self):
        self.screen.fill(cfg.BACKGROUND_COLOR)
        if not self.game.is_over():
            self.draw_next_coin()
        elif self.game.is_over() and self.game.get_winner() is None:
            self.draw_drawn_game()
        else:
            self.draw_winner()
        self.grid_view.update()
        self.screen.blit(self.grid_view.surface, (cfg.BOARD_MARGIN, self.insertion_area_height))
        pygame.display.update()

    def draw_winner(self):
        text = cfg.WINNER[self.lang].format(self.game.get_winner())
        rendered = self.font.render(text, True, cfg.FONT_COLOR)
        x = (self.screen.get_width() - rendered.get_width()) // 2
        y = (self.insertion_area_height - rendered.get_height()) // 2
        self.screen.blit(rendered, (x, y))

    def draw_drawn_game(self):
        text = cfg.DRAWN_GAME[self.lang]
        rendered = self.font.render(text, True, cfg.FONT_COLOR)
        x = (self.screen.get_width() - rendered.get_width()) // 2
        y = (self.insertion_area_height - rendered.get_height()) // 2
        self.screen.blit(rendered, (x, y))

    def draw_next_coin(self):
        center = self.get_center_of_next_coin()
        color = self.get_color()
        draw_coin(self.screen, color, center)

    def get_center_of_next_coin(self):
        chosen_column = self.get_chosen_column()
        dist_between_2_center = 2 * (cfg.COIN_RADIUS + cfg.CELL_MARGIN)
        first_center = cfg.COIN_RADIUS + cfg.CELL_MARGIN + cfg.BOARD_MARGIN
        return chosen_column * dist_between_2_center + first_center, cfg.CELL_MARGIN + cfg.COIN_RADIUS

    def get_coordinate_of(self, row, col):
        x, y = self.grid_view.get_coordinate_of(row, col)
        return x + cfg.BOARD_MARGIN, y + self.insertion_area_height

    def get_color(self):
        if self.game.current_player == 0:
            return cfg.PLAYERS[0][1]
        return cfg.PLAYERS[1][1]

    def get_chosen_column(self) -> int:
        x, y = pygame.mouse.get_pos()
        if x < cfg.BOARD_MARGIN:
            return 0
        if x > cfg.BOARD_MARGIN + self.grid_view.surface.get_width():
            return self.game.grid.cols - 1
        return (x - cfg.BOARD_MARGIN) // self.grid_view.cell_size

    def animate_coin_chute(self):
        color = self.get_color()
        x, y = self.get_center_of_next_coin()
        col = self.get_chosen_column()
        row = self.game.grid.get_free_row(col)
        x_f, y_f = self.get_coordinate_of(row, col)
        while y <= y_f:
            self.screen.fill(cfg.BACKGROUND_COLOR)
            draw_coin(self.screen, color, (x, y))
            self.grid_view.update()
            self.screen.blit(self.grid_view.surface, (cfg.BOARD_MARGIN, self.insertion_area_height))
            pygame.display.update()
            y += self.speed

    @staticmethod
    def display_error_message(msg: str):
        logging.getLogger(View.__class__.__name__).error(msg)
