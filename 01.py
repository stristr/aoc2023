# 91/1231
# 1:37/16:29
from sys import stdin

a, b = 0, 0
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = [str(i) for i in range(10)]
for line in stdin.read().strip().split('\n'):
    adigits, bdigits = [], []
    for i, d in enumerate(line):
        if d in digits:
            adigits += [d]
            bdigits += [d]
        for j, w in enumerate(words):
            if line[i:i+len(w)] == w:
                bdigits += [str(j + 1)]
    a += int(adigits[0] + adigits[-1])
    b += int(bdigits[0] + bdigits[-1])

print('a', a)
print('b', b)
