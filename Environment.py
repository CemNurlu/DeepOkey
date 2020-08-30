# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:45:30 2020

@author: CemPC
"""

from Tile import Tile
from Deck import Deck
from Game import Game

class Environment:
    
    def __init__(self,game):
        self.game = game
    
    
    def throw_action(self,game):
        pass
    #TODO: How to do this? MAKE THIS GYM Compatible after this probs.