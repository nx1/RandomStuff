# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
    
values = {'1': 1,
          '2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 8,
          '9': 9,
          '10': 10,
          'Jack': 11,
          'Queen': 12,
          'King': 13,
          'Ace': 14}

suits = {'Hearts': 0,
         'Diamonds': 1,
         'Spades:': 3,
         'Clubs': 4}

def Random():
    value = np.random.choice(list(values.keys()))
    suit = np.random.choice(list(suits.keys()))
    return value, suit

class Card:
    def __init__(self, suit, value):
            self.suit = suit
            self.value = value
        
    def __repr__(self):
        ret = 'Card: {}, {}'.format(self.suit, self.value)
        return str({'suit:' : self.suit, 'value': self.value})
    
        
class Deck:
    def __init__(self):
        self.cards = [(Card(*Random())) for x in range(52)]
        
    def __repr__(self):
        return repr(self.cards)
    def shuffle(self):
        pass
    
if  __name__ == '__main__':
    c = Card('Hearts', '1')
    
    print(c)
    d = Deck()
    print(d)
    
