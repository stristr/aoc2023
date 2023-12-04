# 181/401
# 3:18/10:21
from sys import stdin

lines = stdin.read().strip().split('\n')
data = list(map(lambda line: (
    list(map(int, value.split()) for value in line.split(': ')[1].split(' | '))), lines))
a = 0
b = {i: 1 for i in range(len(data))}

for i, (winning, have) in enumerate(data):
    winning = len(set(have) & set(winning))
    if winning:
        a += 2 ** (winning - 1)
    for j in range(i + 1, i + 1 + winning):
        b[j] += b[i]

print('a', a)
print('b', sum(b.values()))
