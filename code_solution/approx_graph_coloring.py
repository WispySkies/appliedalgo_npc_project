"""
CS412 Applied Algorithms

Approximated Decision-based Minimum Graph Coloring

Conor McFadden - Declan McCue

this must be polynomial
use greedy random etc whatever works and gets close
"""

from collections import defaultdict


def main():
    K = int(input())
    pairs = [input().split() for _ in range(K)]

    # build color assignments by vertex : color
    assignments = {v: int(k) for v, k in pairs}

    # build adj-list based graph on assignments
    # must it be complete? i.e. all vertices connect
    graph = defaultdict(list)
    for v1, _ in assignments.items():
        for v2, _ in assignments.items():
            # skip edges to self 
            if v1 == v2:
                continue

            graph[v1].append(v2)
            graph[v2].append(v1)


if __name__ == "__main__":
    main()