
from Home import Home
from Platform import Platform
from Tile import Tile

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
        #self.tiles = [[Tile() for i in xrange(width)] for i in xrange(height)]
        self.tiles = [[Tile() for i in range(width)] for i in range(height)]
        self.platforms = []
        self.homes = []

    # I'd like to see Board using __getitem__ and __setitem__
    def __getitem__(self, key):
        x, y = index
        return self.tiles[x][y]

    def __setitem__(self, key, value):
        if not isinstance(value, Tile):
            raise TypeError()
        x, y = key
        self.tiles[x][y] = value
        value.position = key
        if isinstance(value, Platform):
            self.platforms.append(value)
        if isinstance(value, Home):
            self.homes.append(value)

    def addPlatform(self, platform):
        x, y = platform.position()
        self.tiles[x][y] = platform
        self.platforms.append(platform)

    def addHome(self, home):
        x, y = home.position()
        self.tiles[x][y] = home
        self.homes.append(home)