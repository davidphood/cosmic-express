
from Tile import Tile

class Home(Tile):
    def __init__(self, colour):
        self.colour = colour
        self.passenger = None

    def isEmpty(self):
        return False