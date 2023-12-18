# 1631/1739
# 30:39/1:24:23
from sys import stdin

decompose = lambda l, r: sum(L * R for L, R in zip(l[1:], r[2:]))

def dig(data):
    x, y, p, vx, vy = 0, 0, 0, [0], [0]
    for dir, dist in data:
        x += dist if dir == 'R' else -dist if dir == 'L' else 0
        y += dist if dir == 'D' else -dist if dir == 'U' else 0
        vx += [x]; vy += [y]
        p += dist
    assert vx[0] == vx[-1]; assert vy[0] == vy[-1]
    return (p + abs(decompose(vy, vx) - decompose(vx, vy))) // 2 + 1

a, b = [], []
for line in stdin.read().strip().split('\n'):
    dir, dist, hex = line.split()
    a += [(dir, int(dist))]; b += [(
        'R' if hex[-2] == '0' else 'D' if hex[-2] == '1' else 'L' if hex[-2] == '2' else 'U',
        int(hex[2:-2], 16)
    )]

print('a', dig(a))
print('b', dig(b))
