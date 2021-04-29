#!/usr/bin/env python
# driver.py

"""
Let outside methods get their data from this driver function, while also
pushing their output to it
"""

import sys

from oversized_pancake_flipper.function import *
from tidy_numbers.function import *
from bathroom_stalls.function import *

def main():
    """ Take input from standard in, and push results to standard out """

    # Grab method to call from command line
    method = globals()[sys.argv[1]]

    # Read line giving number of examples
    t = int(input())
    for i in range(1, t + 1):

        # Read & parse in a single example, pass to method
        args = input().split(" ")
        c, d = method(*args)

        # Push results to standard out
        print("Case #{}: {} {}".format(i, c, d))

# Called with "./driver.py < large_input.txt > large_output.txt"
main()
