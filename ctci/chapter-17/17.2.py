# -*- coding: utf-8 -*-
'''
Shuffle: Write a method to shuffle a deck of cards. It must be a perfect shuffle
-- in other words, each of the 52! permutations of the deck has to be equally
likely. Assume that you are given a rnadom number generator which is perfect.

[shuffle]
Time: O(N)
Space: O(N)
Notes: Assuming given list of cards is immutable and thus cannot be rearranged,
and also assuming that Python's integer random number generator is "perfect."

[shuffle2]
Time: O(N)
Space: O(1)
'''

import random

def shuffle(cards):
    '''Shuffle this deck of cards without changing the original deck.'''
    shuffled_cards = []
    while len(cards) > 0:
        sel = random.randint(0, len(cards) - 1)
        shuffled_cards.append(cards[sel])
        del cards[sel]
    return shuffled_cards

def shuffle2(cards, depth = 0):
    '''Shuffle these cards, changing the original deck.'''

    # Recurse
    if len(cards) < depth + 1:
        return
    shuffle2(cards, depth + 1)

    # Select index
    end = len(cards) - depth - 1
    sel = random.randint(0, end)

    # Swap
    temp = cards[sel]
    cards[sel] = cards[end]
    cards[end] = temp
    return cards

print(shuffle([x for x in range(1, 53)]))
print(shuffle2([x for x in range(1, 53)]))
