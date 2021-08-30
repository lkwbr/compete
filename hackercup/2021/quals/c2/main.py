"""
It's not quite a traveling salesman problem, not quite a Eulerian trail, but 
certainly a graph optimization problem with a seemingly tricky degree of freedom -
we can alter the graph to add `k` edges that help optimize the objective.

We're going to try to solve this one first before solving the special case (`k = 1`) in the first chapter (`../c1/`). 

We might be able to write a pretty quick solution on solving the optimization 
on just a single graph, and then just feed in different alterations, each with `k`
new edges.  This could be quite expensive.


Constraints:
- 1 <= n <= 50 (nodes)
- 0 <= k <= 50 (addable edges)
- 1 <= a_i, b_i <= n (edge values)
- there are n-1 tunnels

Let's do an analysis here:
    - 
"""


from collections import namedtuple
from functools import reduce

import numpy as np


# NOTE:  Opting for a non-adjacency matrix repr. this time, just for kicks.
mknode = lambda name, reward, next: {
    'name': name, 'reward': reward, 'next': next
}


# NOTE:  No recursion this time.
def special_min_path(nodes: list[dict]):
    """
    Going to do some A* from root back to itself while trying to maximize the 
    reward and not double-trekking edges.
    """
    path_reward = lambda path: sum([n['reward'] for n in set(nodes)])
    root = nodes[0]
    visited_edges = set()
    frontier = [(path_reward([root])), [root]] 
    while frontier:
        working_path = frontier.pop()
        wnode = working_path[-1]
        for n in wnode['next']:
            next_node = nodes[n]
            # Expand frontier
            next_path = 0

    #total = sum([n['reward'] for n in path])
    pass


def add_edge_permutations(graph):
    pass


def solve(edges: np.ndarray, costs: np.ndarray, k: int) -> int: 

    # TODO:  That k shit
    print(sorted(edges.tolist()))
    bucketed_edges = [[] for _ in costs]
    [bucketed_edges[x[0] - 1].append(x[1] - 1) for x in edges]
    print(bucketed_edges)
    nodes = [mknode(name=i, reward=c, next=bucketed_edges[i]) for i, c in enumerate(costs)]

    path, total = special_min_path(nodes)
    exit()


    # TODO:  That search shit

    print(edges) 
    print(costs) 
    print(k) 
    exit()

    """
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
    """


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(x) for x in input().split()]
        costs = np.array([int(x) for x in input().split()])
        edges = np.array([
            [int(x) for x in input().split()] for _ in range(n - 1)
        ])
        x = solve(edges, costs, k)
        print(f'Case #{i}:', x)
