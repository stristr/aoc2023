# 713/718
# 21:27/1:15:23
from sys import stdin
from collections import deque, defaultdict

grid = stdin.read().strip().split('\n')
h, w = len(grid), len(grid[0])
start, goal = (next(((x, y) for x in range(w) if grid[y][x] == '.'), None) for y in (0, h - 1))
deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
valid = lambda x, y: 0 <= x < w and 0 <= y < h and grid[y][x] in '.>v'

def fork(p1, dx, dy, G, q, slopes=False):
    cx, cy, S = *p1, 0
    seen = set([p1])
    while valid(cx + dx, cy + dy):
        cx += dx; cy += dy; S += 1
        seen.add((cx, cy))
        match slopes and grid[cy][cx] in '>v' and grid[cy][cx]:
            case '>':
                if dx == -1:
                    return
                next_deltas = [(1, 0)]
            case 'v':
                if dy == -1:
                    return
                next_deltas = [(0, 1)]
            case _:
                next_deltas = [d for d in deltas if valid(cx + d[0], cy + d[1]) and d != (-dx, -dy)]
        if len(next_deltas) == 1:
            dx, dy = next_deltas.pop()
        elif next_deltas:
            break
    if not any(p2 == (cx, cy) for p2, _ in G[p1]):
        for d in next_deltas:
            q.append(((cx, cy), d))
    G[p1].add(((cx, cy), S))

def graph(slopes=False):
    G, q = defaultdict(set), deque([(start, (0, 1))])
    while q:
        p1, (dx, dy) = q.popleft()
        fork(p1, dx, dy, G, q, slopes=slopes)
    return G

def longest(p, seen, d, G):
    if p == goal:
        return d
    M = max((longest(A, seen + [p], d + D, G) for A, D in G[p] if A not in seen), default=-1)
    return M

print('a', longest(start, [], 0, graph(slopes=True)))
print('b', longest(start, [], 0, graph()))
