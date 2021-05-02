# -*- coding: utf-8 -*-
"""
Binary Tree Balance: Check if any branch on binary tree does not differ by more
than 1 level of depth.

Time: O() -
Space: O() -
"""

from collections import namedtuple


Node = namedtuple('Node', ['left', 'right', 'data'])


def tree_is_balanced(node):
    assert isinstance(node, Node)
    if not node:
        return 0 # leaf node has zero depth
    ldepth, lbal = tree_is_balanced(node.left)
    if not lbal:
        return None, False # short circuit
    rdepth, rbal = tree_is_balanced(node.right)
    if not rbal:
        return None, False # short circuit
    diff = abs(ldepth - rdepth)
    depth = max(ldepth, rdepth) + 1
    return depth, diff <= 1


def run_tests():
    tests = [
        (), False
    ]
    for test_in, test_out in tests:

        pass


if __name__ == '__main__':
    run_tests()