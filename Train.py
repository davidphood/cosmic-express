
from Locomotive import Locomotive
from Carriage import Carriage

from Direction import Direction


class Train:
    def __init__(self, board, numCarriages):
        self.board = board
        self.locomotive = Locomotive(board.entryTrack.position)
        self.carriages = [Carriage() for i in range(numCarriages)]

    def move(self, direction):
        x, y = self.locomotive.position
        if direction == Direction.Up:
            self.locomotive.position = (x, y - 1)
        elif direction == Direction.Down:
            self.locomotive.position = (x, y + 1)
        elif direction == Direction.Left:
            self.locomotive.position = (x - 1, y)
        elif direction == Direction.Right:
            self.locomotive.position = (x + 1, y)
        else:
            raise Exception()

        prevPosition = (x, y)
        for carriage in self.carriages:
            prevPosition, carriage.position = carriage.position, prevPosition
            # Check each carriage against the board to see if they can pick up or drop off a passenger

    def isTrackComplete(self):
        return False