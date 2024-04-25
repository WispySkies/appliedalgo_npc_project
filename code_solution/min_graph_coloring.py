"""
CS412 Applied Algorithms

Decision-based Minimum Graph Coloring

Declan McCue - Conor McFadden


some notes:
reducing problem to can you color a complete graph with K colors
computationally NP-Hard

runtimes on complete graphs:
fixed K, decision on colors >=K, linear
Optimization: O( |V| / sqrt (log|V|) )

Transformations/reductions from minimal maximum matching (Yannakakis and Gavril, 1978)
might be worth a read: https://www.jstor.org/stable/2100648


https://en.wikipedia.org/wiki/Graph_coloring
https://en.wikipedia.org/wiki/Complete_coloring


Presentation problem: Graph coloring is NP-Hard, must reduce to a NP-Complete
Reduce graph coloring to min >= K?

Find: optimal solution of NP-Complete, then find an approximation and do an analysis (must be polynomial)
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