
from functools import reduce
from queue import Queue
import copy


def alchemize(i: int, a: int, b: int) -> tuple[int]:
    assert a < b
    if i < a < b:
        # Alchemy doesn't work here
        return None
    x, y = 0, 0
    if i > a:
        x = i - a
    if i > b:
        y = i - b 
    return x, y


def solve(n: int, a: int, b: int, freqs: list[int]) -> int:
    pass 
    


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        n, a, b = [int(x) for x in input().split()]
        freqs = [int(x) for x in input().split()]
        result = solve(freqs)
        print('Case #{}: {}'.format(i, result))


main()
