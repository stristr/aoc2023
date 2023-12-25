# 139/129
# 15:47/15:53
from sys import stdin
from itertools import combinations
from collections import deque, defaultdict

edges = defaultdict(set)
for line in stdin.read().strip().split('\n'):
    for node in line[5:].split():
        edges[line[:3]].add(node)
        edges[node].add(line[:3])

def network(us, neighbors):
    q, N = deque([us]), set()
    while q:
        node = q.popleft()
        for wire in neighbors[node]:
            if wire not in N:
                q.append(wire); N.add(wire)
    return N

def expand(us, them, capacity, neighbors, capacities):
    if us == them:
        return capacity

    cuts = 0
    while neighbors[us]:
        node = neighbors[us].pop()
        new_capacity = expand(node, them, capacities[us][node], neighbors, capacities)
        cuts += new_capacity
        capacities[us][node] -= new_capacity
        capacities[node][us] += new_capacity
    return cuts

def get_cuts(us, them, capacities):
    distances = {n: 0 if n == us else None for n in edges}
    neighbors, q = {n: set() for n in edges}, deque([us])
    while q:
        n1 = q.popleft()
        if n1 == them:
            return neighbors, expand(us, them, None, neighbors, capacities)
        for n2, capacity in capacities[n1].items():
            if not capacity:
                continue
            if distances[n2] is None:
                distances[n2] = distances[n1] + 1
                neighbors[n1].add(n2)
                neighbors[n2].add(n1)
                q.append(n2)
    return neighbors, 0

def sever(us, them):
    cuts, capacities = 0, {n1: {n2: 1 for n2 in neighbors} for n1, neighbors in edges.items()}
    while True:
        neighbors, new_cuts = get_cuts(us, them, capacities)
        cuts += new_cuts
        if cuts > 3:
            return None
        elif not new_cuts:
            return network(us, neighbors)

for n1, n2 in combinations(edges.keys(), 2):
    if N := sever(n1, n2):
        print('a', len(N) * (len(edges) - len(N)))
        break
