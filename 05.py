# 144/322
# 9:11/37:08
from sys import stdin

input = stdin.read().strip().split('\n\n')
seeds = [int(x) for x in input[0].split(': ')[1].split()]
data = [[list(map(int, line.split())) for line in lines.split('\n')[1:]] for lines in input[1:]]

a, b  = seeds.copy(), []
ranges = [(l, l + d) for l, d in [seeds[i:i + 2] for i in range(0, len(seeds), 2)]]

for rules in data:
    a, b = [
        next((dst + seed - src for dst, src, d in rules if src <= seed < src + d), seed)
        for seed in a
    ], []
    for dst, src, d in rules:
        L, R = src, src + d
        # Capture range intersections.
        b += [(dst + max(l, L) - src, dst + min(r, R) - src) for l, r in ranges if l < R and L < r]
        # Reduce remaining ranges.
        ranges = [(l, r) for l, r in ranges if l > R or r < L] + \
            [(l, L) for l, r in ranges if l < L < r] + \
            [(R, r) for l, r in ranges if l < R < r]
    ranges += b

print('a', min(a))
print('b', min(l for l, _ in b))
