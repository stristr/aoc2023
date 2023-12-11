# 1101/972
# 14:31/20:13
from sys import stdin
from itertools import product, combinations

lines = stdin.read().strip().split('\n')
h, w = len(lines), len(lines[0])
galaxies = [(x, y) for x, y in product(range(w), range(h)) if lines[y][x] == '#']
cols = [x for x in range(w) if all(lines[y][x] == '.' for y in range(h))]
rows = [y for y in range(h) if all(lines[y][x] == '.' for x in range(w))]
manhattan = lambda p1, p2, factor: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + \
    (factor - 1) * sum(p1[0] < x < p2[0] or p2[0] < x < p1[0] for x in cols) + \
    (factor - 1) * sum(p1[1] < y < p2[1] or p2[1] < y < p1[1] for y in rows)
print('a', sum(manhattan(l, r, 2) for l, r in combinations(galaxies, 2)))
print('b', sum(manhattan(l, r, 1000000) for l, r in combinations(galaxies, 2)))
