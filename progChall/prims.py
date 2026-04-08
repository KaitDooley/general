#!/usr/bin/env python3

# Exercise: 16-A: MST

import collections
import heapq
import sys

# Type Aliases

Graph    = dict[str, dict[str, int]]
Visited  = dict[str, str]
Frontier = list[tuple[int, str, str]]

# Build Graph

def read_graph() -> Graph:
    ''' Read in undirected graph '''
    g: Graph = collections.defaultdict(dict)

    for line in sys.stdin:
        source, target, weight = line.split()
        g[source][target] = int(weight)
        g[target][source] = int(weight)
    return g

# Compute MST

def compute_mst(g: Graph) -> Visited:
    frontier = [(0, start, start)]
    visited  = {}
    start    = list(g.keys())[0]

    # TODO
    while frontier:
        weight, target, source = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = source
    
        for neighbor, cost in g[target].items():
            heapq.heappush(frontier, (cost, neighbor, target))

    del visited[start]
    return visited

# Main Execution

def main():
    # Read Graph
    g = read_graph()

    # Compute MST
    m = compute_mst(g)

    # Print Weight and Edges
    edges = sorted((min(p), max(p)) for p in m.items())

    weight = sum(g[s][t] for s, t in edges)

    print(weight)
    for s, t in edges:
        print(s, t)

if __name__ == '__main__':
    main()
