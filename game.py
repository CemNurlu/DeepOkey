from Tile import Tile
from Deck import Deck
import random

class Game:
    """
    Main Game class for starting and initializing the game.


    #ARGUEMENTS

        ended: Boolean, game continue state.

        tilelist: List, list for storing of not in use tile objects

        decklist: List, list for storing deck objects




    #FUNCTIONS

        generate_tiles: Makes tiles.
            Input: None
            Output: List of Tile objects



        generate_decks: Removes tiles from tilelist and add them to decks in decklist.
            Input: None
            Output: List of Deck objects

        generate_joker
            Input: None
            Output: Tile object

    """



    def __init__(self):
        self.game_end = False
        self.tilelist = self.generate_tiles()
        self.decklist = self.generate_decks()
        self.joker = self.generate_joker()

    def generate_tiles(self):
        _tiles = []
        for colour in range(4):
            for number in range(1,14):
                 # Generate 2 tiles and add both to the tiles list
                 _tiles.extend([Tile(colour,number),Tile(colour,number)])
        return(_tiles)

    def generate_decks(self):
        _decklist = []

        # Generate decks and add the tiles
        for i in range(4):
            _decklist.append(Deck(i+1,[]))

        # Move tiles
        for i in range(4):
            #First player gets 1 tile more
            if i == 0:
                tilecount = 15
            else:
                tilecount = 14

            for j in range(tilecount):
                #Pick a tile at random
                tile = random.choice(self.tilelist)

                # Add it to the deck
                _decklist[i].append(tile)

                # Remove it from the tilelist
                self.tilelist.remove(tile)

        return(_decklist)


    # IDEA: should generate_joker function return tile object or list?
    def generate_joker(self):
        tile = random.choice(self.tilelist)

        # Add it to the deck

        # Remove it from the tilelist
        # FIXME: Not sure if this actually works, never ran the code yet, will have to check and fix or make sure.
        if tile.number == 13:
            next_number = 1
        else:
            next_number = tile.number + 1


        self.tilelist.remove(tile)

        joker = Tile(tile.colour,next_number)

        return(joker)

g = Game()
for tile in g.tilelist:
    print(tile.colour, tile.number)
print(g.joker)