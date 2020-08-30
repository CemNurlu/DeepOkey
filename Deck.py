class Deck:
    def __init__(self, playernumber,tiles):
        self.playernumber = playernumber
        self.tiles = tiles
    
    def append(self, tile):
        self.tiles.append(tile)