
from Tile import Tile
from Track import EntryTrack, ExitTrack
from Home import Home
from Platform import Platform

# We can set up a board from a string
# It represents and matrix of squares
# Each square is an object?
# This is lightweight, the tracks, train and monsters can be separate
# - Since they are part of the searching
# What we want from this class:
# - List of all platforms
# - List of all destination (house? box? home? whatever we're calling them)
# - Get entry square
# - Get exit square
# - Tests for creating Board from string and check that items are where we expect
# - Success is when we reach the exit square and all houses are full
# -- All platforms and train will be empty too


class Board:
    def __init__(self, width, height):
        self.tiles = [[Tile() for y in range(height)] for x in range(width)]
        self.entryTrack = None
        self.exitTracks = []
        self.homes = []
        self.platforms = []

    def __getitem__(self, key):
        x, y = key
        return self.tiles[x][y]

    def __setitem__(self, key, value):
        if not isinstance(value, Tile):
            raise TypeError()
        x, y = key
        self.tiles[x][y] = value
        value.position = key
        if isinstance(value, EntryTrack):
            assert(self.entryTrack == None)
            self.entryTrack = value
        elif isinstance(value, ExitTrack):
            self.exitTracks.append(value)
        elif isinstance(value, Platform):
            self.platforms.append(value)
        elif isinstance(value, Home):
            self.homes.append(value)
