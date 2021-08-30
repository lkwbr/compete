"""
This problem seems sort of like a graph problem.

My thinking is that, since we have some tractable bounds and we are
essentially given an incomplete distance metric we can compute a variant of an
adjacency matrix, which instead of explicit edges, measures the shortest path between any two characters.  It's already tractable with the 26^2 memory slots, and we need to do a bounded computation on each cell.

There's a lot of opportunity for pruning, but I don't think we'll need it.
"""


import numpy as np


VOWELS = {'a', 'e', 'i', 'o', 'u'}
ALPHABET = np.array([chr(i + ord('a')) for i in range(ord('z') - ord('a') + 1)])


def compute_distance(
    a: str,
    b: str,
    adj_matrix: list[list],
    visited: set = None,
    depth: int = 0
) -> int:
    """Return number of transitions from two characters `a` -> `b`;
    return `-1` if there exists none.

    NOTE:  Could do bidirectional search to limit time complexity.
    NOTE:  Could also build up the entire distance matrix using DP.
    """
    a_i = ord(a) - ord('a')
    b_i = ord(b) - ord('a')
    #print(depth * '-', ALPHABET[a_i], ALPHABET[b_i])
    visited = visited or set()
    if a_i == b_i:
        # Edges to yourself are 0 weight
        return 0
    if adj_matrix[a_i][b_i]:
        # An edge between a and b was found
        return 1
    # Search for shortest path from a to b
    #best_path = (None, None) 
    best_path = (None, -1) 
    for a_j, col in enumerate(adj_matrix[a_i]):
        #print(depth * '-', a_j, col, best_path)
        if col and (a_i, a_j) not in visited:
            #print(depth * '-', a_j, col, best_path)
            visited.add((a_i, a_j))
            c = chr(a_j + ord('a'))
            #import copy; copy.deepcopy(visited)
            d = compute_distance(c, b, adj_matrix, visited, depth + 1)
            if d > -1:
                d += 1
                if not best_path[0] or d < best_path[1]:
                    best_path = (col, d)
    return best_path[1]


def solve(s: str, trans: list) -> int:
    # Compute lookups once
    s = s.lower()
    trans = set([t.lower() for t in trans])
    char_freqs = np.array([
        len([s_c for s_c in s if ord(s_c) - ord('a') == i]) 
        for i, _ in enumerate(ALPHABET) 
    ])
    s_indices = np.array(sorted(set([ord(c) - ord('a') for c in s])))  

    #######
    np.set_printoptions(edgeitems=30, linewidth=120)
    """
    print(s)
    print(char_freqs)
    print(ALPHABET)
    """
    #######

    # Build up unweighted, directed adjacency matrix
    adj_matrix = np.array([
        [
            1 if chr(ord('a') + i) + chr(ord('a') + j) in trans
            else 0
            for j, _ in enumerate(ALPHABET)
        ] 
        for i, _ in enumerate(ALPHABET) 
    ])

    #print(adj_matrix)

    ######


    import networkx as nx
    from pyvis.network import Network
    G = nx.from_numpy_array(adj_matrix, create_using=nx.MultiDiGraph)
    tx_dict = {i: x for (i, x) in enumerate(ALPHABET)}
    G = nx.relabel.relabel_nodes(G, tx_dict)
    #nt = Network('500px', '500px')
    nt = Network('100%', '100%', directed=True)
    # populates the nodes and edges data structures
    nt.from_nx(G)
    nt.show('nx.html')
    #print(G)

    # Quick test:
    
    """
    from itertools import permutations, combinations_with_replacement
    poss = sorted(list(set(combinations_with_replacement(ALPHABET, 2)).union(set(permutations(ALPHABET, 2)))))
    reachable = [] 
    for a, b in poss:
        comb = a + b
        dist = compute_distance(a, b, adj_matrix)
        print(a, b, dist)
        if comb in trans:
            assert dist == 1
        if dist > -1:
            reachable.append((a, b, dist))
    print('reachable:')
    print(np.array(reachable))
    exit()
    """
    ######

    # Compute (directed) distance matrix between all characters, 
    # the rows being the start nodes and the columns being the end nodes. 
    #print('building distance matrix...', flush=True)
    dist_matrix = np.array([
        [
            compute_distance(chr(ord('a') + i), chr(ord('a') + j), adj_matrix) 
            for j, _ in enumerate(ALPHABET)
        ] 
        for i, _ in enumerate(ALPHABET)
    ])
    #print('done...', flush=True)

    """
    print(dist_matrix)

    import numpy as np
    print(np.array(adj_matrix))
    x = compute_distance('a', 'z', adj_matrix)
    print(x)
    print(trans)
    assert x == 8
    exit()

    print(s_indices)
    print(weighted_slimmed_dist_matrix)

    print('trans:', sorted(list(trans)))
    """



    #print('--------')
    #print(s)
    #print(slimmed_dist_matrix)
    #print(weighted_slimmed_dist_matrix)

    # To achieve "consistency", the column of dist_matrix represents how
    # "fast" each unique character (in ther respective row) can achieve each
    # column character.  We need to not just consider the distance for 
    # transforming a row character to a column character, but how many times
    # that needs to happen per character.  That's why we use `char_freqs` 
    # here.
    slimmed_dist_matrix = dist_matrix[s_indices, :] 
    slimmed_char_freqs = np.reshape(char_freqs[s_indices], (len(s_indices), 1))
    weighted_slimmed_dist_matrix = slimmed_dist_matrix * slimmed_char_freqs
    # Find the lowest cost column reachable by all characters in the string.
    best_char = (None, -1)
    tmp = []
    for i, col in enumerate(zip(*weighted_slimmed_dist_matrix)):
        if any([freq_cost < 0 for freq_cost in col]):
            # There is a character in the string which cannot reach the column 
            # (target) character.
            continue
        cost = sum(col)
        if best_char[0] is None or best_char[1] > cost:
            best_char = (i, cost)

    #assert 'z' == ALPHABET[best_char[0]]
    #print(best_char[0], ALPHABET[best_char[0]])
    return best_char[1]


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        s = input()
        k = int(input())
        trans = [input() for _ in range(k)]
        #if i != 7: continue
        x = solve(s, trans)
        print(f'Case #{i}:', x)
