"""
This problem seems sort of like a graph problem.

My thinking is that, since we have some tractable bounds and we are
essentially given an incomplete distance metric we can compute a variant of an
adjacency matrix, which instead of explicit edges, measures the shortest path between any two characters.  It's already tractable with the 26^2 memory slots, and we need to do a bounded computation on each cell.

There's a lot of opportunity for pruning, but I don't think we'll need it.
"""


VOWELS = {'a', 'e', 'i', 'o', 'u'}


def compute_distance(a: str, b: str, adj_matrix: list[list], visited: set = None, depth: int = 0) -> int:
    """Return number of transitions from two characters `a` -> `b`;
    return `None` if there exists none.

    NOTE:  Could do bidirectional search to limit time complexity.
    """
    a_i = ord(a) - ord('a')
    b_i = ord(b) - ord('a')

    visited = visited or set()

    #print('>' * (depth + 1), a, b)

    if a_i == b_i:
        # Edges to yourself are 0 weight
        return 0
    if adj_matrix[a_i][b_i]:
        # An edge between a and b was found
        return 1
    # Search for shortest path from a to b
    best_path = (None, None) 
    for a_j, col in enumerate(adj_matrix[a_i]):
        if col and (a_i, a_j) not in visited:
            visited.add((a_i, a_j))
            c = chr(a_j + ord('a'))
            d = compute_distance(c, b, adj_matrix, visited, depth + 1)
            if d:
                d += 1
                if not best_path[0] or d < best_path[1]:
                    best_path = (col, d)
    return best_path[1]


def solve(s: str, trans: list) -> int:
    # Compute lookups once
    s = s.lower()
    trans = set([t.lower() for t in trans])

    # Build up unweighted, directed adjacency matrix
    adj_matrix = [
        [
            1 if chr(ord('a') + i) + chr(ord('a') + j) in trans
            else 0
            for j in range(ord('z') - ord('a') + 1)
        ] 
        for i in range(ord('z') - ord('a') + 1)
    ]

    #print(trans)
    #import numpy as np; print(np.array(adj_matrix))

    # Compute (directed) distance matrix between all characters, 
    # the rows being the start nodes and the columns being the end nodes. 
    dist_matrix = [
        [
            compute_distance(chr(ord('a') + i), chr(ord('a') + j), adj_matrix) 
            for j in range(ord('z') - ord('a') + 1)
        ] 
        for i in range(ord('z') - ord('a') + 1)
    ]

    #import numpy as np; print(np.array(dist_matrix))
    #exit()

    s_indices = set([ord(s_c) - ord('a') for s_c in s])
    dist_matrix = [
        row 
        for i, row in enumerate(dist_matrix) 
        if i in s_indices
    ]

    import numpy as np; print(np.array(dist_matrix))

    best_char = (None, -1)
    for i, col in enumerate(zip(*dist_matrix)):
        if None not in col:
            cost = sum(col)
            if best_char[0] is None or best_char[1] > cost:
                best_char = (i, cost)
                #print(col)

    return best_char[1]


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        s = input()
        k = int(input())
        trans = [input() for _ in range(k)]

        if i != 7: continue

        x = solve(s, trans)
        print(f'Case #{i}:', x)
