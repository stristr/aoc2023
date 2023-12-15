# 223/717
# 2:39/18:21
from sys import stdin
from functools import reduce

codes, boxes, h = stdin.read().strip(), [[] for _ in range(256)], {}
HASH = lambda s: reduce(lambda a, b: ((a + ord(b)) * 17) % 256, s, 0)

for code in codes.split(','):
    if '=' in code:
        rval, lval = code.split('=')
        hash, value = HASH(rval), int(lval)
        if rval not in h:
            boxes[hash] += [rval]
        h[rval] = value
    else:
        rval = code[:-1]
        if rval in h:
            boxes[HASH(rval)].remove(rval)
            del h[rval]

print('a', sum(HASH(code) for code in codes.split(',')))
print('b', sum((HASH(code) + 1) * (boxes[HASH(code)].index(code) + 1) * h[code] for code in h))
