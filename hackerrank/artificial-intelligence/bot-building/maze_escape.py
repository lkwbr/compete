#!/usr/bin/env python
'''Escape from an arbitrary maze with only partial observations of the world and
no concept of memory.

The board changes as you make movements, such that the moving "forward" (UP)
will move you in the direction you moved in your prior action. For example,
starting in the world facing up, moving LEFT in the first move and then moving
RIGHT in the second will move you once to the left an once up, with respect to
the upwards world.

Hardcoded solutions have been winning more on HackerRank than general
solutions. Let's not stoop to their level.
'''

import random

def move(obs):
    '''Deterministically output best direction to move given the observable
    `obs` 3x3 units.

    Our approach is to move clockwise throughout the board until we get to the
    entrance. Note that we can only observe the 8 surrounding cells (3x3 -
    center bot position) and we have no possibility of recalling previous
    moves/positions.

    The assumption is that we can traverse the whole space from the walls and
    eventually the exit/door will be found.
    '''
    group_count = 0 # 1 = wall, 2 = corner, 3 = divet
    moves = [(0, 1, 'LEFT'), (1, 0, 'UP'), (2, 1, 'RIGHT'), \
              (1, 2, 'DOWN')]
    for u in moves + moves[:1]: # full 360 degree check (inclusive)
        d = obs[u[1]][u[0]]
        if d == 'e':
            return u[2] # exit
        elif d == '#':
            group_count += 1
        elif d == '-':
            if group_count > 0:
                return u[2]
    return random.choice(moves)[2]

def parse():
    '''Parse HackerRank input.'''
    player_id = int(input())
    observation = [[j for j in input().strip()] for i in range(3)]
    return observation

observation = parse()
print(move(observation))
