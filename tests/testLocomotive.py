
import unittest

from Board import Board
from Colour import Colour
from Direction import Direction
from Home import Home
from Locomotive import Locomotive
from Platform import Platform

class TestLocomotive(unittest.TestCase):
    def testLevel1(self):
        board = Board(8, 7)
        board[1, 2] = Platform(Colour.Purple)
        board[6, 4] = Home(Colour.Purple)
        self.assertFalse(board[1, 2].isEmpty())
        self.assertFalse(board[6, 3].isEmpty())
        self.assertTrue(board[1, 3].isEmpty())

        # We need to place the exit locations/tracks
        # * Possibly placing a track directly, instead of via a train, makes it an exit position
        # * Possibly any track placed before a locomotive is an exit position (use the term position instead of location)
        # Then there are some options to take here:
        # 1. Place the locomotive (on the start position), the locomotive then places a track whenever it moves
        # 2. Keep the locomotive separate to the board and just have it act on the board
        #    * or have it create a separate track so the board remains the same, but the track changes with our search
        # 3. Have a type of Track that's a TrackExit

        locomotive = Locomotive(1)
        board[0, 3] = locomotive
        locomotive.move(Direction.Right)
        locomotive.move(Direction.Right)
        locomotive.move(Direction.Right)
        locomotive.move(Direction.Right)
        locomotive.move(Direction.Right)
        locomotive.move(Direction.Right)
        self.assertFalse(locomotive.isTrackComplete())
        locomotive.move(Direction.Right)
        self.assertFalse(locomotive.isTrackComplete())
