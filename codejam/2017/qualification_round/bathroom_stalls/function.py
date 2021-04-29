# function.py

import math, queue

class RangeNode:

    def __init__(self, a, b, parent = None, depth = 0):

        # Node stuff
        self.parent = None
        self.children = []
        self.is_split = False
        self.depth = depth

        # Range info
        self.a = a
        self.b = b
        self.center = self.__center()
        self.range = self.__range()

    def left_right_space(self):
        ls = self.center - self.a
        rs = self.b - self.center
        return ls, rs

    def max(self):
        """ Breadth-first search through tree for max node """

        node_queue = queue.Queue()
        node_queue.put(self)

        # Dummy starting max variable
        curr_max = (None, -1)

        while not node_queue.empty():

            # Node at top of queue
            curr_node = node_queue.get()

            # Only scrape max from leaf nodes
            if not curr_node.is_split:

                # The moment we encounter a node that is less than the current max,
                # we know we've found our max - so, quit and return that max
                if curr_node.range < curr_max[1]: break
                curr_max = (curr_node, curr_node.range)

            # Add children to queue
            for child in curr_node.children:
                node_queue.put(child)

        return curr_max[0]

    def split(self):
        """ Split and create two of subset children """

        # TODO: Return center point, along with number of open stalls on left
        # and right

        # Don't split if we can't
        if self.range < 2: return None, None

        # Split-off to two new ranges on either side of center
        left_range = RangeNode(self.a, self.center - 1, parent = self, \
            depth = self.depth + 1)
        right_range = RangeNode(self.center + 1, self.b, parent = self, \
            depth = self.depth + 1)
        self.children.append(left_range)
        self.children.append(right_range)
        self.is_split = True

        return left_range, right_range

    def __range(self): return (self.b - self.a) + 1
    def __center(self): return math.ceil((self.a + self.b) / 2)

def bathroom_stalls(*args):

    # Grab params
    num_stalls = int(args[0])
    num_people = int(args[1])
    num_handled = 0

    # Startoff the only range being the entire row of stalls
    root_node = RangeNode(1, num_stalls)
    current_split_range = None

    # Add all the people!
    for p in range(num_people):

        # Get max range node in tree
        current_range_node = root_node.max()

        # Split that range up into two new ones!
        current_range_node.split()
        num_handled += 1

    return current_range_node.left_right_space()
