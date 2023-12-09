# 1507/938
# 10:49/12:17
from sys import stdin
from functools import reduce
from operator import mul

def parse_color(s):
    n, color = s.split(' ')
    return int(n), color

def parse_line(line):
    game, rest = line[5:].split(': ')
    return int(game), [[parse_color(s) for s in pair.split(', ')] for pair in rest.split('; ')]

all_colors = ['red', 'green', 'blue']
limits = dict(zip(all_colors, [12, 13, 14]))
product = lambda l: reduce(mul, l, 1)

data = map(parse_line, stdin.read().strip().split('\n'))
a, b = 0, 0
for game, colors in data:
    maxes = {
        COLOR: max(n for draws in colors for n, color in draws if color == COLOR)
        for COLOR in all_colors
    }
    a += game if all(maxes[COLOR] <= limits[COLOR] for COLOR in all_colors) else 0
    b += product(maxes.values())

print('a', a)
print('b', b)
