class Player:
    """Manage a player for the game Tic Tac Toe."""

    def __init__(self, symbol):
        """Assigns given string argument to the symbol attribute."""
        self.symbol = symbol

    def get_move(self):
        """Return a list containing two integers representing a xy position."""
        print("Enter two digits between 1 and 3 with no whitespace separating them.")
        while True:
            xy_position = input("XY position to place your mark on the board: ")
            xy_position = list(xy_position)
            # Check if given xy position is within the game board.
            if 1 <= int(xy_position[0]) <= 3 and 1 <= int(xy_position[1]) <= 3:
                return xy_position
            else:
                print("Hmm, I need to pick a xy position inside the games board...")
