# Second case
from functools import reduce
import math
def find_summers(l: list, s: int, n: int) -> list:
		"""Recursively iterate through list left-to-right, subdividing the problem, all in O(n^2)."""
		if n == 1:
				return [s] if s in l else [None]
		for	i, _ in enumerate(l):
				u = find_summers(l[:i + 1], s - l[i], n - 1)
				if None not in u:
						return [l[i]] + u  
		return [None]

l = [int(li) for li in open('day-1.txt')]
r = find_summers(l, 2020, 3)
print('>', *r, math.prod(r))
exit()

# First case
t = 2020
l = [int(li) for li in open('day-1.txt')]
p = set([t - x for x in l])
m = [x for x in l if x in p][0]
a, b = m, t - m
r = a * b 
assert a + b == 2020 and (a in l) and (b in l)
print('>', a, b, r)
