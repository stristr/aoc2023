# 483/358
# 18:13/21:34
from sys import stdin
from itertools import product
from collections import deque

lines = stdin.read().strip().split('\n')
h, w = len(lines), len(lines[0])
m = {complex(x, y): lines[y][x] for x, y in product(range(w), range(h))}

def energize(dir, loc):
    q, seen, energized = deque([(dir, loc)]), set([(dir, loc)]), set([loc])
    def go(dir, nextloc):
        if nextloc not in m or (dir, nextloc) in seen:
            return
        q.append((dir, nextloc)); seen.add((dir, nextloc)); energized.add(nextloc)

    while q:
        dir, loc = q.popleft()
        if (not dir.imag and m[loc] in '.-') or (not dir.real and m[loc] in '.|'):
            go(dir, loc + dir)
        elif m[loc] in '/\\':
            dir *= (1j if not dir.real else -1j) * (1 if m[loc] == '/' else -1)
            go(dir, loc + dir)
        else:
            go(dir * 1j, loc); go(dir * -1j, loc)
    return len(energized)

print('a', energize(1, complex(0, 0)))
print('b', max(
    *[energize(1, complex(0, y)) for y in range(h)],
    *[energize(1j, complex(x, 0)) for x in range(w)],
    *[energize(-1, complex(w - 1, y)) for y in range(h)],
    *[energize(-1j, complex(x, h - 1)) for x in range(w)],
))
