# 154/259
# 12:48/46:02
from sys import stdin
from itertools import product
from collections import deque

lines = stdin.read().strip().split('\n')
h, w = len(lines), len(lines[0])
m = {(x, y): lines[y][x] for x, y in product(range(w), range(h))}
sx, sy = next(k for k, v in m.items() if v == 'S')
cangonorth = lambda x, y: m[x, y] in '|JLS' and (x, y - 1) in m and m[x, y - 1] in '|7F'
cangosouth = lambda x, y: m[x, y] in '|7FS' and (x, y + 1) in m and m[x, y + 1] in '|JL'
cangoeast = lambda x, y: m[x, y] in '-FLS' and (x + 1, y) in m and m[x + 1, y] in '-7J'
cangowest = lambda x, y: m[x, y] in '-7JS' and (x - 1, y) in m and m[x - 1, y] in '-FL'
m[sx, sy] = 'L' if cangonorth(sx, sy) and cangoeast(sx, sy) else \
    'J' if cangonorth(sx, sy) and cangowest(sx, sy) else \
    '7' if cangosouth(sx, sy) and cangowest(sx, sy) else \
    'F' if cangosouth(sx, sy) and cangoeast(sx, sy) else \
    '|' if cangonorth(sx, sy) and cangosouth(sx, sy) else \
    '-' if cangoeast(sx, sy) and cangowest(sx, sy) else None
assert m[sx, sy] is not None

a, q = {(sx, sy): 0}, deque([(sx, sy)])
def travel(x, y, d):
    if (x, y) not in a:
        a[(x, y)] = d + 1
        q.append((x, y))

while q:
    x, y = q.popleft()
    loc, d = m[(x, y)], a[(x, y)]
    if cangoeast(x, y):
        travel(x + 1, y, d)
    if cangowest(x, y):
        travel(x - 1, y, d)
    if cangosouth(x, y):
        travel(x, y + 1, d)
    if cangonorth(x, y):
        travel(x, y - 1, d)

print('a', max(a.values()))

# expand
loop = [(2*x, 2*y) for x, y in a.keys()] + \
    [(2*x + 1, 2*y) for x, y in a.keys() if cangoeast(x, y)] + \
    [(2*x - 1, 2*y) for x, y in a.keys() if cangowest(x, y)] + \
    [(2*x, 2*y + 1) for x, y in a.keys() if cangosouth(x, y)] + \
    [(2*x, 2*y - 1) for x, y in a.keys() if cangonorth(x, y)]
m = {
    **{(2*x, 2*y): v for (x, y), v in m.items()},
    **{(x, y): '#' for x, y in product(range(2*w), range(2*h)) if x % 2 == 1 or y % 2 == 1},
}

b, visited = set(), set(loop)
deltas = [(dx, dy) for dx, dy in product([-1, 0, 1], [-1, 0, 1]) if not (dx == dy == 0)]
for xx, yy in product(range(w), range(h)):
    if (2*xx, 2*yy) in loop or (2*xx, 2*yy) in visited:
        continue
    # find path to outside
    q, flood, outside = deque([(2*xx, 2*yy)]), set([(2*xx, 2*yy)]), False
    while q:
        x, y = q.popleft()
        for dx, dy in deltas:
            X, Y = x + dx, y + dy
            if (X, Y) in visited:
                continue
            visited.add((X, Y))
            if X == 0 or X == 2*(w - 1) or Y == 0 or Y == 2*(h - 1):
                outside = True
            if (X, Y) in m and (X, Y) not in loop:
                q.append((X, Y))
                flood.add((X, Y))
    if not outside:
        b |= flood

print('b', sum(m[x, y] != '#' for x, y in b))
