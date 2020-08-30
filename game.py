from Tile import Tile
from Deck import Deck
import random

class Game:
    """
    Main Game class for starting and initializing the game.


    #ARGUMENTS

        game_end: Boolean, game continue state.

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
        self.generate_joker()
        self.decklist = self.generate_decks()
        
    # --INITIALIZATIONS FOR THE GAME--
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
        for i in range(1,5):
            _decklist.append(Deck(i,[]))

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


    def generate_joker(self):
        #generate joker
        joker_colour = random.choice(range(0,4))
        joker_number = random.choice(range(1,14))
        
        #Add joker to the tiles
        self.tilelist.extend([Tile(joker_colour, joker_number,is_joker = True),
                             Tile(joker_colour, joker_number,is_joker = True)])
        
        #Find the tile opened to the ground and remove it
        if joker_number == 13:
            opened_tile_number = 1
        else:
            opened_tile_number = joker_number + 1
        
        
        for i in self.tilelist:
            if i.colour == joker_colour and i.number == opened_tile_number:
                self.tilelist.remove(i) ##TODO: Maybe later save this to a position for visualization?
                break
        
        # --GAME ACTIONS--
        class action():
            def throw_tile(self,tile):
                pass
        
        # --STATE FUNCTIONS--
        def read_state(self,playernumber):
            pass
        
            
            

