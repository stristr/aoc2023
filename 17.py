# 543/1262
# 25:50/1:07:51
from sys import stdin
from itertools import product
from queue import PriorityQueue

lines = stdin.read().strip().split('\n')
h, w = len(lines), len(lines[0])
m, goal = {(x, y): int(lines[y][x]) for x, y in product(range(w), range(h))}, (w - 1, h - 1)

def minimize(minstep=1, maxstep=3):
    q = PriorityQueue()
    heat, loc, dirs = 0, (0, 0), ((0, 1), (1, 0))
    best = {(loc, dirs): heat}
    q.put((heat, loc, dirs))
    while q:
        heat, loc, dirs = q.get()
        if loc == goal:
            return heat
        for dx, dy in dirs:
            nextdirs, nextloc, nextheat = ((dy, dx), (-dy, -dx)), loc, heat
            for step in range(1, maxstep + 1):
                nextloc = (nextloc[0] + dx , nextloc[1] + dy)
                if nextloc not in m:
                    break
                nextheat += m[nextloc]
                if step < minstep or (
                    (nextloc, nextdirs) in best and nextheat >= best[(nextloc, nextdirs)]
                ):
                    continue
                best[(nextloc, nextdirs)] = nextheat
                q.put((nextheat, nextloc, nextdirs))

print('a', minimize())
print('b', minimize(minstep=4, maxstep=10))
