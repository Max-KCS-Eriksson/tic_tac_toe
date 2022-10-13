class Player:
    """Manage a player for the game Tic Tac Toe."""

    def __init__(self, symbol):
        """Assigns given string argument to the symbol attribute."""
        self.symbol = symbol

    def get_move(self):
        """Return a tuple containing two integers representing a xy position."""
        xy_position = input("XY position to place your mark on the board: ")

        return tuple(xy_position)
