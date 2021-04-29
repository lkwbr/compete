#!/usr/bin/env python

'''
Unit tests for my precious HackerRank submissions.

NOTE: All coordinates are in (row, col) order.
'''

import os
import sys
import logging
import unittest

import botclean_large
import botclean_large_STOLEN

def get_tests(folder):
    '''Return input and output lists seperately, corresponding by index.

    Assuming the inputted folder location has 'input' and 'output'
    subdirectories containing input and output .txt files whose names
    correspond by a zero-based index.

    Discovering all filenames under the directories and then collecting the
    lines of data within them.
    '''
    files = [['\\'.join([folder, x, y]) for y in \
        os.listdir('{}/{}' .format(folder, x))] for x in ['input', 'output']]
    tests = [[open(x, 'r').readlines() for x in y] for y in files]
    return tests

@unittest.skip('Attempting different approach.')
class TestBotCleanLarge(unittest.TestCase):
    '''Unit tests for BotClean Large problem.'''
    test_folder = botclean_large.TEST_CASES
    def setUp(self):
        self.log = logging.getLogger('TestBotCleanLarge')
        self.tests = get_tests(self.test_folder)
    def test_bfs(self):
        ins, outs = self.tests
        test_range = (3, 4) # [a, b)
        for i in range(*test_range):
            # Parse test input, output
            im, aus = ins[i], outs[i] # hey hey, Deutchland
            pos = [int(x) for x in im[0].strip().split()]
            dims = [int(x) for x in im[1].strip().split()]
            board = [x.strip().split() for x in im[2:]]
            ausgabe = tuple(int(x) for x in aus[0].strip().split())
            # Attempt to find dirt cell
            dirt_cell = botclean_large.search(pos, dims, board)
            # Check with output
            self.assertEqual(dirt_cell, ausgabe)
            # Output traversed board to file
            botclean_large.output_board(board)

class TestBotCleanLargeSTOLEN(unittest.TestCase):
    '''Unit tests for BotClean Large STOLEN solution.'''
    test_folder = botclean_large.TEST_CASES
    def setUp(self):
        self.log = logging.getLogger('TestBotCleanLarge')
        self.tests = get_tests(self.test_folder)
    def test_stolen(self):
        ins, outs = self.tests
        test_range = (0, 1) # [a, b)
        for i in range(*test_range):
            # Parse test input, output
            im, aus = ins[i], outs[i] # hey hey, Deutchland
            pos = [int(x) for x in im[0].strip().split()]
            dims = [int(x) for x in im[1].strip().split()]
            board = [x.strip().split() for x in im[2:]]
            ausgabe = tuple(int(x) for x in aus[0].strip().split())
            # Attempt to find dirt cell
            dirt_cell = botclean_large_STOLEN.finish(pos, dims, board)
            # Check with output
            self.assertEqual(dirt_cell, ausgabe)
            # Output traversed board to file
            botclean_large.output_board(board)

# Enable logging and run tests
if __name__ == '__main__':
    logging.basicConfig(stream = sys.stderr)
    logging.getLogger('TestBotCleanLarge').setLevel(logging.DEBUG)
    unittest.main()
