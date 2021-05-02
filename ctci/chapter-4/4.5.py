# -*- coding: utf-8 -*-
"""
Check BST: Check if any branch on binary tree does not differ by more
than 1 level of depth.

Time: O() -
Space: O() -
"""

from collections import namedtuple


Node = namedtuple('Node', ['left', 'right', 'data'])


def tree_is_bst(node):
    assert isinstance(node, Node)
    # TODO

def run_tests():
    tests = [
        (), False
    ]
    for test_in, test_out in tests:

        pass


if __name__ == '__main__':
    run_tests()