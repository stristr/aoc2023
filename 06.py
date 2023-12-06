# ?/?
# 6:57/10:39
from sys import stdin
from re import findall
from functools import reduce
from math import ceil, floor, sqrt
from operator import mul

lines = stdin.read().strip().split('\n')
ints = lambda s: [int(n) for n in findall(r'\d+', s)]
data = list(zip(ints(lines[0]), ints(lines[1])))
product = lambda l: reduce(mul, l, 1)
concat = lambda ns: int(''.join(str(n) for n in ns))
discriminant = lambda t, d: sqrt(t**2 - 4*d)
roots = lambda t, d: (ceil((t - discriminant(t, d)) / 2), floor((t + discriminant(t, d)) / 2))

print('a', product(r - l + 1 for l, r in [roots(t, d) for t, d in data]))

l, r = roots(concat([t for t, _ in data]), concat([d for _, d in data]))
print('b', r - l + 1)
