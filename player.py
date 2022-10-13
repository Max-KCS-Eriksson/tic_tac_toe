class Player:
    """Manage a player for the game Tic Tac Toe."""

    def __init__(self, symbol):
        """Assigns given string argument to the symbol attribute."""
        self.symbol = symbol

    def get_move(self):
        """Return a tuple containing two integers representing a xy position."""
        print("Enter two digits between 0 and 2 with no whitespace separating them.")
        while True:
            xy_position = input("XY position to place your mark on the board: ")
            xy_position = tuple(xy_position)
            # Check if given xy position is within the game board.
            if 0 <= int(xy_position[0]) <= 2 and 0 <= int(xy_position[1]) <= 2:
                return xy_position
            else:
                print("Hmm, I need to pick a xy position inside the games board...")
