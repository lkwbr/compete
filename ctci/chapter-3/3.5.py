# -*- coding: utf-8 -*-
'''
Sort Stack: Design a sorted stack such that the smallest elements are on the top.

Time: O(N) for insertion, O(1) for removal
Space: O(N) - at any given moment, only N elements exist within the main or temporary stacks
Note: This stack's ordering is stable.
'''

from random import shuffle

class SortedStack:
    def __init__(self):
        self.stack = []
        self.refstack = []
    def push(self, e):
        while len(self.stack) > 0 and self.peek() <= e:
            v = self.stack.pop()
            self.refstack.append(v)
        self.stack.append(e)
        while len(self.refstack) > 0:
            v = self.refstack.pop()
            self.stack.append(v)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isempty(self):
        return len(self.stack) == 0

# Tests
if __name__ == '__main__':
    sorted_stack = SortedStack()
    nums = [x for x in range(100)]
    shuffle(nums)
    for e in nums:
        sorted_stack.push(e)
    nums.sort()
    for e in nums:
        v = sorted_stack.pop()
        assert e == v