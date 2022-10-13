import subprocess

from player import Player


class TicTacToe:
    """Manage a game of Tic Tac Toe."""

    def __init__(self):
        """Init the game and create game resources."""
        # Init players.
        player1 = Player("Player_1", "X")
        player2 = Player("Player_2", "O")
        # Static attributes.
        self.players = [player1, player2]

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
                xy_position = player.get_move()
                # Subtract 1 from x and y positions to account for indices.
                xy_position[0] = int(xy_position[0]) - 1
                xy_position[1] = int(xy_position[1]) - 1

                # Validate player move.
                if self._is_xy_board_position_free(xy_position):
                    self._update_game_board(player.symbol, xy_position)
                else:
                    print("That tile is already taken.")
                    continue

                # Redraw the game board.
                self._draw_game_board()

                # Check for a winner after each players move.
                winner_symbol = self._check_for_winner()
                if winner_symbol:
                    break
            # Break main loop.
            if winner_symbol:
                break
        # Announce winner.
        for player in self.players:
            if player.symbol == winner_symbol:
                winner = player.name
                print(f"\nThe winner is {winner}!")
                break

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
        column_header = "   1 2 3 "
        border = "  +-+-+-+"
        print(column_header)
        print(border)
        row_num = 1
        for row in self.game_board.values():
            # Print row with side borders and separators.
            board_row = "|".join(row)
            print(f"{row_num} |{board_row}|")
            # Print bottom border.
            print(border)

            # Increment row_num for next iteration.
            row_num += 1

    def _update_game_board(self, player_symbol, xy_position):
        """
        Update the game board with a players symbol and chosen X-Y position.
        A tuple or list is expected as an argument for the xy_position parameter.
        """
        # Unpack xy_position.
        x_position, y_position = xy_position[1], xy_position[0]

        # Place players symbol on game board.
        self.game_board[x_position][y_position] = player_symbol

    def _is_xy_board_position_free(self, xy_position):
        """
        Return a boolean value depending of if the given xy_position on the game board
        is free.
        """
        # Unpack xy_position.
        x_position, y_position = xy_position[1], xy_position[0]

        if self.game_board[x_position][y_position] == " ":
            return True
        else:
            return False

    def _check_for_winner(self):
        """Check any player has three in a row on the game board."""
        winner_symbol = None

        # Check for diagonal wins.
        if (
            self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2]
            and self.game_board[1][1] != " "
        ) or (
            self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]
            and self.game_board[1][1] != " "
        ):
            # Center tile will contain winners symbol regardless of diagonal direction.
            winner_symbol = self.game_board[1][1]
            return winner_symbol

        # Check for horizontal win.
        for row in self.game_board.values():
            if row[0] == row[1] == row[2] and row[0] != " ":
                winner_symbol = row[0]
                return winner_symbol

        # Check for vertical wins.
        for column in self.game_board.keys():
            if (
                self.game_board[0][column]
                == self.game_board[1][column]
                == self.game_board[2][column]
                and self.game_board[0][column] != " "
            ):
                winner_symbol = self.game_board[0][column]
                return winner_symbol


if __name__ == "__main__":
    # Create a game instance and run the game.
    ttt = TicTacToe()
    ttt.run_game()
