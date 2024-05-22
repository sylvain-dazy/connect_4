import logging

# View
USER_ACTION_INVITE_COMMAND = "{} > "

EMPTY_CELL_SYMBOL = " "
BOTTOM_SEPARATOR = "-"
CELL_SEPARATOR = "|"

QUIT_ACTION = {"en": "q",
               "fr": "q"}
NEW_GAME_ACTION = {"en": "n",
                   "fr": "n"}
MENU = {"en": "Enter the column number, {} to stat a new game or {} to exit the game",
        "fr": "Entrez le numéro de la colonne, {} pour commencer un nouveau jeu ou {} pour quitter le jeu"}

# Common
LOG_LEVEL = logging.INFO
LANG = "fr"
WINNER = {"en": "{} has won the game",
          "fr": "{} a gagné la partie !"}
DRAWN_GAME = {"en": "It's a draw !",
              "fr": "Match nul !"}
ROWS = 6
COLS = 7
COUNT_TO_WIN = 4
PLAYERS = [("Sylvain", "S"), ("Cathy", "J")]
