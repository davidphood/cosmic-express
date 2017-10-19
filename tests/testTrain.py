
# Run with 'py -m unittest tests.testTrain'
# Or for all tests 'py -m unittest discover'

import unittest

from Board import Board

from Home import Home
from Platform import Platform

from Track import EntryTrack, ExitTrack
from Train import Train

from Colour import Colour
from Direction import Direction

class TestTrain(unittest.TestCase):
    def testLevel1(self):
        board = Board(8, 7)
        board[0, 3] = EntryTrack()
        board[7, 3] = ExitTrack()
        board[1, 2] = Platform(Colour.Purple)
        board[6, 4] = Home(Colour.Purple)
        self.assertFalse(board[1, 2].isEmpty())
        self.assertFalse(board[6, 4].isEmpty())
        self.assertTrue(board[1, 3].isEmpty())

        # We need to place the exit locations/tracks
        # * Possibly placing a track directly, instead of via a train, makes it an exit position
        # * Possibly any track placed before a locomotive is an exit position (use the term position instead of location)
        # Then there are some options to take here:
        # 1. Place the locomotive (on the start position), the locomotive then places a track whenever it moves
        # 2. Keep the locomotive separate to the board and just have it act on the board
        #    * or have it create a separate track so the board remains the same, but the track changes with our search
        # 3. Have types of Track that are ExitTrack and EntryTrack
        #    * When we create a Train (consisting of Locomotive + Carriages) we can pass the board to it
        #    * The Train uses the location of the EntryTrack from the board as it's own location
        #    * Moving the train drops a track (if no track already there)
        #    * That way the Train, Locomotive and Carriages aren't on the board, they float above / use the board instead

        train = Train(board, 1)
        train.move(Direction.Right)
        train.move(Direction.Right)
        train.move(Direction.Right)
        train.move(Direction.Right)
        train.move(Direction.Right)
        train.move(Direction.Right)
        self.assertFalse(train.isTrackComplete())
        train.move(Direction.Right)
        self.assertTrue(train.isTrackComplete())
