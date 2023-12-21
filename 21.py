# 961/237
# 11:22/1:32:25
from sys import stdin
from itertools import product

def parse_line(line):
    return list(line)

lines = stdin.read().strip().split('\n')
assert len(lines) == len(lines[0])
d = len(lines)
start = next((x, y) for x, y in product(range(d), range(d)) if lines[y][x] == 'S')
adjacencies = lambda x, y: [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
is_rock = lambda x, y: lines[y % d][x % d] == '#'

reached, i, sample = set([start]), 0, []
cycle = 26501365 % d; target = 26501365 // d

while len(sample) < 3:
    i += 1
    plots = set()
    for x, y in reached:
        for xx, yy in adjacencies(x, y):
            if is_rock(xx, yy) or (xx, yy) in reached or (xx, yy) in plots:
                continue
            plots.add((xx, yy))
    reached = plots
    if i % d == cycle:
        sample += [len(reached)]
    if i == 64:
        print('a', sum(0 <= x < d and 0 <= y < d for x, y in reached))

# Quadratic regression from samples at 0, 1, 2.
c = sample[0]; b = (4 * sample[1] - 3 * c - sample[2]) // 2; a = sample[1] - b - c
print('b', a * target ** 2 + b * target + c)
