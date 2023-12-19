# 403/469
# 16:08/42:44
from sys import stdin
from re import findall, search
from functools import reduce
from collections import deque
from math import prod

class Range:
    def __init__(self, l, r):
        self.l = l; self.r = r

    reject = lambda self, op, n: Range(max(self.l, n), self.r) if op == '<' else Range(self.l, min(self.r, n))
    accept = lambda self, op, n: Range(self.l, min(self.r, n - 1)) if op == '<' else Range(max(self.l, n + 1), self.r)
    size = lambda self: self.r - self.l + 1 if self.l <= self.r else 0

def parse_rule(condition):
    if match := search(r'[<>]', condition):
        op = match.group()
        l, r = condition.split(op)
        r, outcome = r.split(':')
        return (l, op, int(r), outcome)
    else:
        return condition

def parse_rules(line):
    name, rest = line.split('{')
    return name, [parse_rule(condition) for condition in rest[:-1].split(',')]

def parse_part(line):
    return {k: Range(int(v), int(v)) for k, v in findall(r'([a-z])=(\d+)', line)}

top, bottom = stdin.read().strip().split('\n\n')
workflows = {name: parsed for name, parsed in [parse_rules(line) for line in top.split('\n')]}
parts = [parse_part(line) for line in bottom.split('\n')]

def reduce(m):
    q, accepted = deque([('in', m)]), []
    while q:
        wf, m = q.popleft()
        if wf == 'R':
            continue
        if wf == 'A':
            accepted.append(m)
            continue
        for rule in workflows[wf]:
            if isinstance(rule, tuple):
                l, op, r, outcome = rule
                M = m.copy()
                M[l] = m[l].accept(op, r)
                q.append((outcome, M))
                m[l] = m[l].reject(op, r)
            else:
                q.append((rule, m))
    return accepted

print('a', sum(
    sum(r.l for r in m.values()) if all(r.size() for r in m.values()) else 0 for p in parts for m in reduce(p)))
print('b', sum(
    prod(rng.size() for rng in m.values()) for m in reduce({k: Range(1, 4000) for k in 'xmas'})))
