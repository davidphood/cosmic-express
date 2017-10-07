
from Tile import Tile

class Platform(Tile):
    def __init__(self, colour):
        self.colour = colour
        self.passenger = Passenger(colour)

    def isEmpty(self):
        return False