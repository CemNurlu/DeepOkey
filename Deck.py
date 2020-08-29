class Deck:
    def __init__(self, playernumber,tiles, is_joker = False):
        self.playernumber = playernumber
        self.tiles = tiles
        self.is_joker = is_joker
    
    def append(self, tile):
        self.tiles.append(tile)