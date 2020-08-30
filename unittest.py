# -*- coding: utf-8 -*-
"""
Unit tests:
ADD MORE
@author: CemPC
"""

from Game import Game


import unittest

class TestStringMethods(unittest.TestCase):
    

    def test_deck_count(self):
        self.assertEqual(len(g.decklist), 4)

    def test_tile_count_deck(self):
        tilecount = []
        for deck in g.decklist:
            tilecount.append(len(deck.tiles))
        self.assertEqual(tilecount, [15,14,14,14])
    
    def test_total_tile_count(self):
        self.assertEqual(len(g.tilelist) + sum([15,14,14,14]) , 105)


if __name__ == '__main__':
    g = Game()
    unittest.main()

