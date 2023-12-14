# 325/411
# 5:56/26:55
from sys import stdin
from itertools import product

lines = stdin.read().strip().split('\n')
h, w = len(lines), len(lines[0])
m = {(x, y): lines[y][x] for x, y in product(range(w), range(h))}
load = lambda: sum(h - y for (_, y), v in m.items() if v == 'O')
serialize = lambda: (''.join(m[x, y] for x, y in product(range(w), range(h))), load())

directions = {
    'N': [1, False, 0, -1],
    'W': [0, False, -1, 0],
    'S': [1, True, 0, 1],
    'E': [0, True, 1, 0],
}

def slide(d):
    axis, reverse, dx, dy = directions[d]
    for x, y in sorted(m.keys(), key=lambda k: k[axis], reverse=reverse):
        if m[x, y] != 'O':
            continue
        while 0 <= y + dy < h and 0 <= x + dx < w and m[x + dx, y + dy] not in '#O':
            m[x, y] = '.'
            x += dx; y += dy
            m[x, y] = 'O'

slide('N')
print('a', load())

history, loop = [None], None

while True:
    for d in 'NWSE':
        slide(d)

    key = serialize()
    if key in history:
        loop = history.index(key), len(history)
        break
    history.append(key)

print('b', history[loop[0] + ((1000000000 - loop[0]) % (loop[1] - loop[0]))][1])
