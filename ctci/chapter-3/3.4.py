# -*- coding: utf-8 -*-
'''
Queue via Stacks: Emulate queue behavior using just two stacks.

Time: O(N) - insertion and deletion
Space: O(N) - at any given moment, only N elements exist within either stack
'''

class MyQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    def enqueue(self, e):
        while len(self.dequeue_stack) > 0:
            v = self.dequeue_stack.pop()
            self.enqueue_stack.append(v)
        self.enqueue_stack.append(e)
    def dequeue(self):
        while len(self.enqueue_stack) > 0:
            v = self.enqueue_stack.pop()
            self.dequeue_stack.append(v)
        v = self.dequeue_stack.pop()
        return v
    def peek(self):
        while len(self.enqueue_stack) > 0:
            v = self.enqueue_stack.pop()
            self.dequeue_stack.append(v)
        return self.dequeue_stack[-1]
    def isempty(self):
        return len(self.dequeue_stack) + len(self.enqueue_stack) == 0

# Tests
if __name__ == '__main__':
    my_queue = MyQueue()
    for i in range(100):
        my_queue.enqueue(i)
        v = my_queue.peek()
        print(i, v)
        assert v == 0
    my_queue.enqueue(100)
    for i in range(101):
        v = my_queue.dequeue()
        print(i, v)
        assert i == v