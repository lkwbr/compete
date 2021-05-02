# -*- coding: utf-8 -*-
'''
Check Permutation: Given two strings, write a method to decide if one is a
permutation of the other.

Time: O(N)
Space: O(N)
'''

def check_permutation(a, b):
    '''Check the distrubition of frequencies for each character to
    determine if they are permutations of one another.'''

    # Permutations must have the same number of characters.
    if len(a) != len(b):
        return False

    # Build frequency dictionary of a.
    ad = dict()
    for e in a:
        ad[e] = ad.get(e, 0) + 1

    # Check for same distrubition of frequencies in b.
    bd = dict()
    for e in b:
        bd[e] = bd.get(e, 0) + 1
        # Check for dissimilar characters.
        if ad[e] is None:
            return False
        # See if there's too much of any character.
        if bd[e] > ad[e]:
            return False

    # At this point: both strings are the same length, have the same
    # types of characters, and have no exceeding number of characters.
    # Therefore, a and b are permutations of one another.
    return True

print(check_permutation('abca', 'bacc'))
