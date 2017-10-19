
from Tile import Tile


class Track(Tile):
    def isEmpty(self):
        return False


class EntryTrack(Track):
    pass


class ExitTrack(Track):
    def isEmpty(self):
        return True