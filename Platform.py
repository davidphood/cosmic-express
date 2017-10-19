
from Passenger import Passenger
from Tile import Tile


class Platform(Tile):
    def __init__(self, colour):
        self.passenger = Passenger(colour)

    def isEmpty(self):
        return False