# 1526/669
# 20:26/21:58
from sys import stdin
from re import finditer
from itertools import product
from functools import reduce
from collections import defaultdict
from operator import mul

data = stdin.read().strip().split('\n')
h, w = len(data), len(data[0])
deltas = [(dx, dy) for dx, dy in product([-1, 0, 1], [-1, 0, 1]) if not (dx == dy == 0)]
M = defaultdict(set)
parts = [(int(m.group(0)), m.start(), m.end(), y)  for y, line in enumerate(data) for m in finditer(r'\d+', line)]
multiply = lambda l: reduce(mul, l, 1)

for x, y in product(range(w), range(h)):
    if data[y][x].isdigit() or data[y][x] == '.':
        continue
    for number in parts:
        num, start, end, row = number
        for dx, dy in deltas:
            if row == y + dy and start <= x + dx < end:
                M[x, y, data[y][x]].add(number)
                break

print('a', sum(num for num, *_ in set().union(*M.values())))
print('b', sum(multiply(num for num, *_ in part) for (_, _, symbol), part in M.items() if symbol == '*' and len(part) == 2))
