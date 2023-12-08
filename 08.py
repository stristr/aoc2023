# 249/134
# 4:29/11:19
from sys import stdin
from re import findall
from itertools import cycle
from math import lcm

lines = stdin.read().strip().split('\n')
turns, m = lines[0], {x: (y, z) for x, y, z in [findall(r'[A-Z0-9]{3}', line) for line in lines[2:]]}

a, ptr = 0, 'AAA'
for t in cycle(turns):
    if ptr == 'ZZZ':
        break
    a += 1
    ptr = m[ptr][0] if t == 'L' else m[ptr][1]

b, ptrs = 0, [k for k in m.keys() if k[-1] == 'A']
cycles = [0] * len(ptrs)
for t in cycle(turns):
    if all(c > 0 for c in cycles):
        break
    for i, c in enumerate(ptrs):
        if cycles[i] > 0:
            continue
        if c[-1] == 'Z':
            cycles[i] = b
    b += 1
    ptrs = [m[c][0] if t == 'L' else m[c][1] for c in ptrs]

print('a', a)
print('b', lcm(*cycles))
