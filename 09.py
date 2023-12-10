# 929/858
# 8:43/11:29
from sys import stdin

data = [[int(x) for x in line.split()] for line in stdin.read().strip().split('\n')]
windowed = lambda vals, n: list(zip(*[vals[i:] for i in range(n)]))
a = lambda vals: 0 if all(x == 0 for x in vals) else vals[-1] + a([r - l for l, r in windowed(vals, 2)])
b = lambda vals: 0 if all(x == 0 for x in vals) else vals[0] + b([r - l for l, r in windowed(vals, 2)])
print('a', sum(a(vals) for vals in data))
print('b', sum(b(vals) for vals in data))
