
from functools import reduce
from queue import Queue
import copy
import random


def sort_and_dedup(l: list) -> list:
    l = sorted(l) 
    s = set()
    new_l = []
    for x in l: 
        if x not in s:
            new_l.append(x)
        s.add(x)
    return new_l


def grab_gaps(n: int, k: int, l: list) -> list:

    # Insert the lowest and highest values
    if l[0] != 1:
        l = [1] + l 
    if l[-1] != k:
        l = l + [k]

    assert len(l) >= 2

    # Sliding window to get ranges
    ranges = []
    for i in range(len(l) - 1):
        c_range = (l[i], l[i + 1])
        ranges.append(c_range)

    return l, ranges


def get_top_idx(m: int, l: list) -> tuple:
    top = []
    for _ in range(m):
        i = l.index(max(l))
        top.append(i)
        l = l[:i] + l[i + 1:]
    return tuple(top)


def solve(n: int, k: int, tix: list) -> float:

    if k == 1:
        return 0.0

    # You want to widen the threshold of values that you are closest to,
    # which means, with your two picks, either
    #   - snag the two widest gaps
    #   - snag the same large gap
    ftix = sort_and_dedup(tix)

    # Extract the gaps
    ftix2, gaps = grab_gaps(n, k, ftix)
    dists = [b - a - 1 for a, b in gaps]

    assert len(dists) == len(gaps) == len(ftix2) - 1

    if sum(dists) == 0:
        # No place to pick!
        return 0.0

    # NOTE:  Just pick two top highest for now
    picked_gap_indices = get_top_idx(2, gaps) 
    picked_gaps = [gaps[pgi] for pgi in picked_gap_indices if dists[pgi] > 0]

    # Find the best way to pick in the gaps that maximizes num_closest
    # TODO:  Out of the two biggest gaps, we can compare them and
    #        see if we should just edge a single gap, which would be two tests.
    num_closest = 0 
    picks = []
    for a, b in picked_gaps:
        pick = a + 1 
        left_count = (b - pick) // 2
        if a not in tix:
            # We added a (leftmost)
            left_count = pick
        else:
            left_count = (pick - a) // 2 if pick - a > 2 else 0 # middle numbers don't count
        if b not in tix:
            # We added b (rightmost
            right_count = b - pick
        else:
            right_count = (b - pick) // 2 if b - pick > 2 else 0
        clst = 1 + left_count + right_count 
        num_closest += clst
        picks.append(pick)

    # Return probability
    prob = num_closest / k
    return prob
    


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        n, k = [int(x) for x in input().split()]
        tix = [int(x) for x in input().split()]
        result = solve(n, k, tix)
        print('Case #{}: {}'.format(i, result))


def test():
    """
    1≤T≤100.
    1≤N≤30.
    1≤Pi≤K, for all i.

    1≤K≤10^9
    """
    # edge cases
    N = 1
    K = 1
    tix = [random.randint(1, K) for _ in range(N)]
    result = solve(N, K, tix)
    print('Case #{}: {}'.format(0, result))

    N = 1
    K = 20
    tix = [random.randint(1, K) for _ in range(N)]
    result = solve(N, K, tix)
    print('Case #{}: {}'.format(0, result))

    N = 2
    K = 20
    tix = [random.randint(1, K) for _ in range(N)]
    result = solve(N, K, tix)
    print('Case #{}: {}'.format(0, result))

    # rando
    #T = random.randint(1, 100)
    T = int(1e9)
    for i in range(1, T + 1):
        N = random.randint(1, 30) 
        K = random.randint(1, int(1e9))
        tix = [random.randint(1, K) for _ in range(N)]
        result = solve(N, K, tix)
        #print('Case #{}: {}'.format(i, result))


#main()
test()
