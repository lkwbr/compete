# -*- coding: utf-8 -*-
'''
URLify: Write a method to replace all spaces in a string with '%20'. You may
assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.

Time: O(N)
Space: O(N)
Notes: The space can be increased to O(1) with this algorithm if we instead are
passed a character array (or any other mutable type), as character arrays can be
modified in-place whereas strings cannot.
'''

def urlify(s, l):
    '''Encode string for URL in one pass from right to left.'''

    # Make s mutable
    s = list(s)

    # Copy index
    c = l - 1
    # Paste index
    p = l - 1

    if s[c] != ' ':
        # String needs no whitespace encoding, because no additional space
        # was given
        return s

    # Find first copyable character
    while s[c].isspace():
        c -= 1

    # When c overlaps with p, we know there is no more encoding left to do,
    # as the given trailing whitespace in `s` has been all used up
    while c < p:
        if s[c] == ' ':
            # Encode the whitespace
            s[p] = '0'
            s[p - 1] = '2'
            s[p - 2] = '%'
            p -= 3
        else:
            # Copy the character directly
            s[p] = s[c]
            p -= 1
        c -= 1

    return ''.join(s)

# Tests
test_str = '30 fuck dude this is crazy          '
print(test_str)
print(urlify(test_str, len(test_str)))