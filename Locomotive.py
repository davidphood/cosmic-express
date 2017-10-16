
from Carriage import Carriage
from Direction import Direction

class Locomotive:
    def __init__(self, numCarriages):
        self.carriages = [Carriage() for i in range(numCarriages)]
        self.board = None
        self.position = None

    def move(self, direction):
        x, y = self.position
        if direction == Direction.Up:
            self.position = (x, y - 1)
        elif direction == Direction.Down:
            self.position = (x, y + 1)
        elif direction == Direction.Left:
            self.position = (x - 1, y)
        elif direction == Direction.Right:
            self.position = (x + 1, y)
        else:
            raise Exception()

        prevPosition = (x, y)
        for carriage in self.carriages:
            prevPosition, carriage.position = carriage.position, prevPosition
            # Check each carriage against the board to see if they can pick up or drop off a passenger

    def isTrackComplete(self):
        return False