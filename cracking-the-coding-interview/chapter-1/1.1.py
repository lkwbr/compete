# -*- coding: utf-8 -*-

'''Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
'''

import string

def is_unique_1(input_string, sym_dict):
    '''Check for duplicates of each symbol in the given string. Assume
    list of allowable characters stays constant for all inputs.

    Time: O(nm) where n = len(input_string), m = len(sym_dict)
    Space: O(1)
    '''
    for sym in sym_dict:
        sym_freq = 0
        for c in input_string:
            if sym == c:
                sym_freq += 1
            if sym_freq > 1:
                return False
    return True

def is_unique_2(input_string):
    '''Check for duplicates of each symbol in the given string using a
    Boolean lookup array - avoiding the use of a hashtable.

    Time:
    Space: 
    '''
    low, high = (input_string[0]) * 2
    for c in input_string:
        if ord(c) < ord(low):
            low = c
        elif ord(c) > ord(high):
            high = c
    bool_ref = [False] * (ord(high) - ord(low))
    print(bool_ref)
    

print(is_unique_1('abmcdefd', string.printable))
print(is_unique_2('abmcdefd'))
