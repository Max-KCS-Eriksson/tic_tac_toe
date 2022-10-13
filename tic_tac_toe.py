import subprocess

from player import Player


class TicTacToe:
    """Manage a game of Tic Tac Toe."""

    def __init__(self):
        """Init the game and create game resources."""
        # Static attributes.
        self.player1 = Player()
        self.player2 = Player()
        self.players = [self.player1, self.player2]

        # Dynamic attributes.
        self._start_new_game()
        self.player1_score = 0
        self.player2_score = 0

    def run_game(self):
        """The main loop of the game."""
        # Draw the empty game board.
        self._draw_game_board()

        while True:
            for player in self.players:
                # Player make a move.

                # Update Screen.
                self._update_game_board()
                self._draw_game_board()
                # Check for a winner.

    def _start_new_game(self):
        """Starts a new game with an empty game board."""
        # Three empty rows and columns.
        self.game_board = {
            0: [" ", " ", " "],
            1: [" ", " ", " "],
            2: [" ", " ", " "],
        }

    def _draw_game_board(self):
        """Clear the terminal and print the game board."""
        subprocess.run("clear")
        # Print top border.
        border = "+-+-+-+"
        print(border)
        for row in self.game_board.values():
            # Print row with side borders and separators.
            row = "|".join(row)
            print(f"|{row}|")
            # Primt bottom border.
            print(border)

    def _update_game_board(self, player_symbol, xy_position):
        """Update the game board with a players symbol and chosen X-Y position."""
        self.game_board


if __name__ == "__main__":
    # Create a game instance and run the game.
    ttt = TicTacToe()
    ttt.run_game()
