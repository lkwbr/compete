# function.py

import math

class OpenRange:

    def __init__(self, a, b):

        # Keep track of our ranges
        self.a = a
        self.b = b

        self.center = self.__center()
        self.range = self.__range()

    def left_right_space(self):
        ls = self.center - self.a
        rs = self.b - self.center
        return ls, rs

    def split(self):

        # TODO: Return center point, along with number of open stalls on left
        # and right

        # TODO: Make sure we handle ranges of just 1 cell well enough!
        if self.range < 2: return None, None

        # Split-off to two new ranges on either side of center
        left_range = OpenRange(self.a, self.center - 1)
        right_range = OpenRange(self.center + 1, self.b)

        return left_range, right_range

    def __range(self): return (self.b - self.a) + 1
    def __center(self):
        # TODO: Make sure we're rounding right
        center = math.ceil((self.a + self.b) / 2)
        return center

def bathroom_stalls(*args):

    # Grab params
    num_stalls = int(args[0])
    num_people = int(args[1])
    num_handled = 0

    # Startoff the only range being the entire row of stalls
    whole_range = OpenRange(1, num_stalls)
    range_coll = [whole_range]
    current_split_range = None

    # Add all the people!
    for p in range(num_people):

        print(num_handled / num_stalls)

        # Get maximum range in list
        max_range = (None, -1) # (range object, range length)
        split_index = None
        for i, r in enumerate(range_coll):
            if r.range > max_range[1]:
                max_range = (r, r.range)
                split_index = i

        # Split that range up into two new ones!
        current_split_range = max_range[0]
        new_left_range, new_right_range = current_split_range.split()
        insertion = [new_left_range, new_right_range]

        if current_split_range.range < 2:
            num_handled += 1
            insertion = []
        range_coll[split_index:split_index + 1] = insertion

        # TODO: Fix problem with not being able to add all popel

    return current_split_range.left_right_space()
