import logging

from src.main.core.board import Board
from src.main.core.game import Game


class Console:
    def __init__(self, game: Game):
        self.game = game

    def play(self):
        running = True
        while running:
            self.display_game()
            self.display_menu()
            user_action = input("> ")
            if user_action in {"quit", "exit", "end", "close"}:
                running = False
            else:
                column = int(user_action)
                if column <= 0 or column > 7:
                    print("Error")
                else:
                    try:
                        self.game.insert_coin(column - 1)
                    except Board.ColumnIsFullError:
                        print("Column " + str(column) + " is full")
                        logging.getLogger(Console.__name__).error("Column " + str(column) + " is full")

    def display_menu(self):
        if self.game.get_current_color() == "R":
            color = "red"
        else:
            color = "yellow"
        print("It's " + color + " player turn")

    def display_game(self):
        print(" 1 2 3 4 5 6 7 ")
        for row in range(6):
            for col in range(7):
                if self.game.board.grid[row][col] == "R":
                    symbol = "R"
                elif self.game.board.grid[row][col] == "Y":
                    symbol = "Y"
                else:
                    symbol = " "
                print("|" + symbol, end="")
            print("|")
        print("|-|-|-|-|-|-|-|")
