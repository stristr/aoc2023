# <did not compete>
from sys import stdin
from re import findall
from itertools import combinations
import mpmath as mp
import numpy as np

data = [[int(x) for x in findall(r'-?\d+', line)] for line in stdin.read().strip().split('\n')]
S, V, N = [hailstone[:3] for hailstone in data], [hailstone[3:] for hailstone in data], len(data)
LOW, HIGH = 200000000000000, 400000000000000

def collide2d(i, j):
    M = np.array([[V[k][1], -V[k][0]] for k in (i, j)])
    v = np.array([[S[k][0] * V[k][1] - S[k][1] * V[k][0]] for k in (i, j)])
    if np.linalg.det(M) == 0:
        return False
    [x], [y] = np.linalg.inv(M) @ v
    return all(LOW <= e <= HIGH for e in (x, y)) and all(
        t > 0 for t in ((x - S[k][0]) / V[k][0] for k in (i, j)))

def throw3d(i, j, k):
    M = mp.matrix([
        [V[l][1] - V[i][1], V[i][0] - V[l][0], 0, S[i][1] - S[l][1], S[l][0] - S[i][0], 0]
        for l in (j, k)
    ] + [
        [V[l][2] - V[i][2], 0, V[i][0] - V[l][0], S[i][2] - S[l][2], 0, S[l][0] - S[i][0]]
        for l in (j, k)
    ] + [
        [0, V[l][2] - V[i][2], V[i][1] - V[l][1], 0, S[i][2] - S[l][2], S[l][1] - S[i][1]]
        for l in (j, k)
    ])
    v = mp.matrix([
        [(S[i][1] * V[i][0] - S[l][1] * V[l][0]) - (S[i][0] * V[i][1] - S[l][0] * V[l][1])]
        for l in (j, k)
    ] + [
        [(S[i][2] * V[i][0] - S[l][2] * V[l][0]) - (S[i][0] * V[i][2] - S[l][0] * V[l][2])]
        for l in (j, k)
    ] + [
        [(S[i][2] * V[i][1] - S[l][2] * V[l][1]) - (S[i][1] * V[i][2] - S[l][1] * V[l][2])]
        for l in (j, k)
    ])

    [x], [y], [z], *_ts = (mp.powm(M, -1) * v).tolist()
    return int(mp.ceil(x + y + z))

print('a', sum(collide2d(i, j) for i, j in combinations(range(N), 2)))
print('b', throw3d(0, 1, 2))
