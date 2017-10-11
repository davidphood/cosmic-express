
import unittest

from Board import Board
from Colour import Colour
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

        locomotive = Locomotive(1)
        # Ideally board[(0,3)] = locomotive
        board.addLocomotive(0,3, locomotive)
        # Should this be Direction.East?
        locomotive.moveDirection(Direction.Right)
        locomotive.moveDirection(Direction.Right)
        locomotive.moveDirection(Direction.Right)
        locomotive.moveDirection(Direction.Right)
        locomotive.moveDirection(Direction.Right)
        locomotive.moveDirection(Direction.Right)
        # Do we ask the board or the locomotive?
        self.assertFalse(board.isComplete())
        self.assertFalse(locomotive.isFinished())
        locomotive.moveDirection(Direction.Right)
        # Do we ask the board or the locomotive?
        # isComplete, isFinished, isDone?
        self.assertTrue(board.isComplete())
        self.assertFalse(locomotive.isFinished())