"""
Thinking here is that we can just check every column and row independently
for a solution in a pretty brute-force way and build up a global list of sets of 
cells, returning the `len` and `min` `len` of that list.  If the list is empty,
return "Impossible".  Brute force should be tractable here, where 2 <= N < 50 means
we've got something around `2 * 50 * 50 = 5000` operations, which is... cake. 

Am I missing something, or is it really that easy?

Deciding to use numpy, because Google Code Jam supports it.
"""


from functools import reduce

import numpy as np


def build_row_win_sets(
    board: np.ndarray, 
    reverse_coor: bool = False
) -> list[set[tuple]]:
    """Build a list of sets, each representing moves to fill the row up 
    with 1's.
    """
    set_coor = lambda i, j: (i, j) if not reverse_coor else (j, i)
    win_sets = list()
    for i, _ in enumerate(board):
        row = board[i]
        if any([x == -1 for x in row]):
            # Cannot win on this row
            continue
        # Can win here, let's count how many remaining rows we need 
        n_exists = sum([1 for x in row if x == 1])
        n_remains = len(row) - n_exists
        win_set = set([set_coor(i, j) for j, val in enumerate(row) if val == 0])
        win_sets.append(win_set)
    return win_sets 


def solve(board: np.ndarray) -> str: 
    # Get winning row sets of coordinates
    win_sets = build_row_win_sets(board)
    board = board.transpose()
    win_sets += build_row_win_sets(board, reverse_coor=True)
    # Remove duplicates, O(N^2)
    win_sets = list(reduce(
        lambda acc, x: acc + [x] if x not in acc else acc, 
        win_sets, list()
    )) 
    # Tidy up the outputs and send off
    if len(win_sets) == 0:
        return 'Impossible'
    min_moves_to_win = min(map(len, win_sets))
    n_possible_wins = sum([1 for x in win_sets if len(x) == min_moves_to_win])
    return str(min_moves_to_win) + ' ' + str(n_possible_wins) 


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        # Build transformed board
        n = int(input())
        tx = {'X': 1, 'O': -1, '.': 0} 
        board = [[tx[x] for x in list(input())] for _ in range(n)]
        board = np.array(board)
        # Solve board
        x = solve(board)
        print(f'Case #{i}:', x)
