#!/usr/bin/env python
'''Clean a large grid-space of dirty cells as efficiently as possible.
'''

# TODO: Utilize breadth-first search methodology, or redo and use travelling salesman.

import queue

TEST_CASES = 'test-cases/botcleanlarge-testcases'

def search(pos, dims, board):
    '''Simple breadth-first search through the board, seeking always the nearest
    dirty cells. Search process is the following. Note that each "layer" of
    cells is checked in a clock-wise fashion.

                      < ^ ^ ^ >
           < ^ >      < < ^ > >
    b  ->  < b >  ->  < < b > >  ->  etc.
           < v >      < < v > >
                      < v v v >

    Front format witin queue: (alias, start pos, end pos, unit vector from start
    -> end, update vector for front), where the start and end pos lie on the
    same horizontal or vertical line.

    Args:
        pos (list): Position of bot in board in terms of (x, y) using a matrix
        coordinate system.
        dims (list): Dimensions of the board in terms of (height, width).

    Returns:
        tuple: Location of nearest dirty cell.
    '''
    dir_dict = {'left' : '<', 'up': '^', 'right': '>', 'down': 'v' }
    # Utility functions
    safe_int_div = lambda x, y: 0 if y == 0 else x // y
    board_val = lambda x: board[x[1]][x[0]] \
                    if 0 <= x[0] < dims[0] and 0 <= x[1] < dims[1] \
                    else None # index out of bounds
    slide = lambda a, b: (a[0] + b[0], a[1] + b[1])
    component_safe_slide = lambda a, b: safe_slide(safe_slide(a, (b[0], 0)), \
                                                   (0, b[1])) # slide x, slide y
    safe_slide = lambda a, b: slide(a, b) \
                    if board_val(slide(a, b)) is not None \
                    else a # slide out of bounds; keep left operand
    unit_vec = lambda a, b: (safe_int_div(b[0] - a[0], abs(b[0] - a[0])), \
                             safe_int_div(b[1] - a[1], abs(b[1] - a[1])))
    midpoint = lambda a, b: ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2)
    inverse = lambda x: (-x[0], -x[1])
    expand = lambda start, end, update, unit: \
                    (safe_slide(safe_slide(start, inverse(unit)), update), \
                     safe_slide(safe_slide(end, unit), update))
    manhatten_distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    bounded = lambda a, b, c: (a[0] == b[0] == c[0] and (a[1] <= b[1] <= c[1] \
                    or a[1] >= b[1] >= c[1])) or (a[1] == b[1] == c[1] and \
                    (a[0] <= b[0] <= c[0] or a[0] >= b[0] >= c[0]))
    # Sitting on dirty cell already?
    if board_val(pos) == 'd':
        return pos
    # Add fronts to queue in this order: left, top, right, and bottom.
    front_queue = queue.Queue()
    front_queue.put(('left', component_safe_slide(pos, (-1, 1)), \
                    component_safe_slide(pos, (-1, -1)), (0, -1), (-1, 0)))
    front_queue.put(('up', component_safe_slide(pos, (0, -1)), \
                    component_safe_slide(pos, (0, -1)), (1, 0), (0, -1)))
    front_queue.put(('right', component_safe_slide(pos, (1, -1)), \
                    component_safe_slide(pos, (1, 1)), (0, 1), (1, 0)))
    front_queue.put(('down', component_safe_slide(pos, (0, 1)), \
                    component_safe_slide(pos, (0, 1)), (-1, 0), (0, 1)))
    while not front_queue.empty():
        # Enumerate cells within the front (from start to end)
        alias, start, end, unit, update = front_queue.get()
        # Check if pos is in this front (meaning front could project out)
        if bounded(start, pos, end):
            continue
        curr = start
        while True:
            if board_val(curr) == 'd':
                return curr
            board[curr[1]][curr[0]] = dir_dict[alias]
            if curr == end:
                break
            curr = slide(curr, unit)
        # Progress front if it can proceed
        if board_val(slide(midpoint(start, end), update)) is not None:
            # Push the front to its next expansion
            start, end = expand(start, end, update, unit)
            front = (alias, start, end, unit, update)
            front_queue.put(front)
    return None

def act(pos, target):
    '''Make movement toward the target cell from current position.
    '''
    if target is None:  # no dirty cell
        raise ValueError('Board is perfectly clean! No cleaning needed.')
    elif pos == target: # current cell dirty
        return 'CLEAN'
    else: # move to dirty cell
        if pos[1] - target[1] > 0:
            return 'UP'
        elif pos[1] - target[1] < 0:
            return 'DOWN'
        elif pos[0] - target[0] > 0:
            return 'LEFT'
        elif pos[0] - target[0] < 0:
            return 'RIGHT'

def output_board(board):
    '''Print board to new file for observation.
    '''
    with open('traversed_board.txt', '+w') as boardfile:
        for row in board:
            for col in row:
                boardfile.write('%s ' % col)
            boardfile.write('\n')

# Do the daaaaaance.
if __name__ == '__main__':
    pos = list(reversed([int(i) for i in input().strip().split()]))
    dims = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dims[0])]
    target = search(pos, dims, board)
    action = act(pos, target)
    print(action)
