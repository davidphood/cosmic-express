
# We can set up a board from a string
# It represents and matrix of squares
# Each square is an object?
# This is lightweight, the tracks, train and monsters can be separate
# - Since they are part of the searching
# What we want from this class:
# - List of all platforms
# - List of all destination (house? box? whatever we're calling them)
# - Get entry square
# - Get exit square
# - Tests for creating Board from string and check that items are where we expect
# - Success is when we reach the exit square and all houses are full
# -- All platforms and train will be empty too


class Board:
    def __init__( self ):
