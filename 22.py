# 396/568
# 34:48/50:19
from sys import stdin
from re import findall
from itertools import combinations
from collections import defaultdict

def get_bricks(line):
    ints = [int(x) for x in findall(r'\d+', line)]
    return [sorted(tup) for tup in zip(ints, ints[3:])]

intersecting = lambda v1, v2: v1[0] <= v2[0] <= v1[1] or v1[0] <= v2[1] <= v1[1] or \
    v2[0] <= v1[0] <= v2[1] or v2[0] <= v1[1] <= v2[1]

bricks = [get_bricks(line) for line in stdin.read().strip().split('\n')]; n = len(bricks)
bricks.sort(key=lambda v: v[2][0])
above, holding, held = defaultdict(set), defaultdict(set), defaultdict(set)
for i, (x, y, z) in enumerate(bricks):
    for j in range(i):
        if intersecting(x, bricks[j][0]) and intersecting(y, bricks[j][1]):
            above[j].add(i)
    below = [j for j in range(i) if i in above[j]]
    dz = z[0] - (max(bricks[j][2][1] for j in below) + 1 if below else 0)
    bricks[i][2] = (z[0] - dz, z[1] - dz)
for i, j in combinations(range(n), 2):
    if j in above[i] and bricks[i][2][1] == bricks[j][2][0] - 1:
        holding[i].add(j); held[j].add(i)

def damage(i):
    damage = set([i])
    for j in range(i + 1, n):
        if j in held and all(k in damage for k in held[j]):
            damage.add(j)
    return damage

print('a', sum(all(len(held[h]) > 1 for h in holding[i]) for i in range(n)))
print('b', sum(len(damage(i)) - 1 for i in range(n)))
