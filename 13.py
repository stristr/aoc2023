# 813/1085
# 17:42/31:49
from sys import stdin

data = [chunk.split('\n') for chunk in stdin.read().strip().split('\n\n')]
reverse = lambda l: list(reversed(l))
transpose = lambda l: list(zip(*l))
diff = lambda a, b: sum(a[i][j] != b[i][j] for i in range(len(a)) for j in range(len(a[0])))

def find_reflection(lines, d, goal):
    for y in range(1, (d+1) // 2):
        if diff(lines[:y], reverse(lines[y:2*y])) == goal:
            return y

def find_any_reflection(lines, goal):
    h, w = len(lines), len(lines[0])
    if (y := find_reflection(lines, h, goal)) is not None:
        return 100 * y
    if (y := find_reflection(reverse(lines), h, goal)) is not None:
        return 100 * (h - y)
    if (x := find_reflection(transpose(lines), w, goal)) is not None:
        return x
    if (x := find_reflection(reverse(transpose(lines)), w, goal)) is not None:
        return w - x

print('a', sum(find_any_reflection(lines, goal=0) for lines in data))
print('b', sum(find_any_reflection(lines, goal=1) for lines in data))
