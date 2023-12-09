# 929/858
# 8:43/11:29
from sys import stdin

data = [[int(x) for x in line.split()] for line in stdin.read().strip().split('\n')]
a, b = 0, 0
for seq in data:
    seqs = [seq]
    while not all(x == 0 for x in seqs[-1]):
        seqs += [[seqs[-1][i] - seqs[-1][i - 1] for i in range(1, len(seqs[-1]))]]
    for i in range(len(seqs) - 2, -1, -1):
        seqs[i] = [seqs[i][0] - seqs[i+1][0]] + seqs[i] + [seqs[i+1][-1] + seqs[i][-1]]
    a += seqs[0][-1]; b += seqs[0][0]

print('a', a)
print('b', b)
