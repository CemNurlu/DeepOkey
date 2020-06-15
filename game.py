from random import randrange


class Game:
    """All functions necessary for the game, core of the project."""
    
    #TODO:Add OpenAI Gym Integration

    
    def __init__(self):
        
        self.all_tiles, self.joker, self.decks =  self.generate()
        
        self.turn = 0
        
        self.throwntiles =[[] for i in range(4)]

    def generate(self):

        

        """
        4 Suits,
        13 Numbers
        1 Fake
        x2 deck
        Fake is original Joker(Not added as not needed to remove)
        Joker is any tile
        """

        """
        17bit number to represent each tile
        First 4 Numbers Suit, 13 After is Number
        Joker is all 1 bits
        """
        all_tiles=[]
        
        #Generate Joker:
        for i in range(2):
            all_tiles.append((2 ** 17) - 1)
            joker = [randrange(4),randrange(13)]

        #Not Effective but lazy and ok implemantation to generate deck
        #TODO:Fix this.
        for _ in range(2):
            for i in range(4):
                for j in range(13):
                    t = (2 ** (13+i)) + (2 **j)
                    all_tiles.append(t)
                    
        
        
        #Generate Hands of each player
        decks = []
        for i in range(4):
            deck = []
            for _ in range(14):
                t = all_tiles.pop(randrange(len(all_tiles)))
                deck.append(t)
            
            #player 1 who starts gets an extra tile
            if (i==0):
                t = all_tiles.pop(randrange(len(all_tiles)))
                deck.append(t)
            decks.append(deck)
        
        
        return all_tiles,joker,decks
    
    #TODO: FIX THIS.
    def throw(self,thrownTile,playerid):
        tile = self.decks[playerid].pop(thrownTile)
        self.throwntiles[playerid+1].append(tile)
        
    
    def take(self,take,playerid):
        DoTake = take
        
        if DoTake == True:
            self.decks[playerid].append(self.throwntiles[playerid].pop(-1))
        else:
            x = randrange(len(self.all_tiles))
            self.decks[playerid].append(self.all_tiles[x])
            self.all_tiles.remove(x)
        self.showstate(playerid)
            
    
    
    def action(self,playerid, throw=0, take=0):
        if (self.turn == 1):
            #Only throw, no take! shorturl.at/blqBO
            self.throw(throw,playerid)
        else:
            #Take, see what you took, and throw
            print(self.take(take,playerid))
            
            throw = int(input("throw?"))
            
            self.throw(throw,playerid)
        self.turn +=1
            
            
    def showstate(self,playerid):
        return {"playerid":playerid,
                "deck": self.decks[playerid],
                "GroundTiles": self.throwntiles,
                "joker": self.joker,
                "turn": self.turn
                }
    
    #TODO: do next turn!
        
game = Game()
print(game.showstate(1))
i = game.showstate(1)["deck"]
for k in i:
    print(bin(k))


#TODO: Human interpreter for binary to suit and number
#TODO: Inputs to Turns
    
            
        


