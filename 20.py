# 644/1108
# 42:02/1:35:51
from sys import stdin
from collections import deque
from math import lcm

def parse_line(line):
    l, r = line.split(' -> ')
    if l == 'broadcaster':
        return None, l, tuple(r.split(', '))
    return l[0], l[1:], tuple(r.split(', '))

lines = stdin.read().strip().split('\n')
data = [parse_line(line) for line in lines]
flipflops = {id: (False, m) for signal, id, m in data if signal == '%'}
conjunctions = {id: ({
    _id: False
    for _, _id, _m in data if id in _m
}, m) for signal, id, m in data if signal == '&'}
broadcaster = next(sinks for _, id, sinks in data if id == 'broadcaster')

def ping():
    q = deque([(None, id, False) for id in broadcaster])
    lows, highs = [], []
    while q:
        src, id, high = q.popleft()
        if high:
            highs.append(id)
        else:
            lows.append(id)
        if id in flipflops:
            if not high:
                flipflops[id] = (not flipflops[id][0], flipflops[id][1])
                for _id in flipflops[id][1]:
                    q.append((id, _id, flipflops[id][0]))
        elif id in conjunctions:
            tracker, downstreams = conjunctions[id]
            tracker[src] = high
            high = not all(tracker.values())
            for _id in downstreams:
                q.append((id, _id, high))
    return lows, highs


precursors = [k for k, v in conjunctions.items() if 'rx' in v[1]]
assert all(precursor in conjunctions for precursor in precursors)
assert all(k in conjunctions for precursor in precursors for k in conjunctions[precursor][0].keys())
tracking = {k: None  for precursor in precursors for k in conjunctions[precursor][0].keys()}
low, high = 0, 0

i = 0
while not all(tracking.values()):
    i += 1
    lows, highs = ping()
    low += 1 + len(lows); high += len(highs)
    for k in tracking:
        if tracking[k] is not None or k not in lows:
            continue
        tracking[k] = i
    if i == 1000:
        print('a', low * high)

print('b', lcm(*tracking.values()))
