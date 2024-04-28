"""
CS412 Applied Algorithms

Decision-based Minimum Graph Coloring

Declan McCue - Conor McFadden

Some helpful references:

https://en.wikipedia.org/wiki/Graph_coloring
https://en.wikipedia.org/wiki/Complete_coloring
"""

from collections import defaultdict

def color(G, v) -> list[tuple]:
    
    # can color vertex with color
    def is_safe_assignment(vertex, colors, proposed) -> bool:
        for neighbor in G[vertex]:
            if colors[neighbor] == proposed:
                return False
        return True

    # backtracking recursive coloring
    def color_graph(vertex, colors) -> bool:
        print(colors)
        if vertex == len(G):
            return True
        
        for color in range(1, v + 1):
            if is_safe_assignment(vertex, colors, color):
                colors[vertex] = color
                if color_graph(vertex + 1, colors):
                    return True
                colors[vertex] = color
        
        return False

    # iterate over 
    colors = [0] * (len(G) + 1)
    if color_graph(0, colors):
        return [(vertex, colors[vertex]) for vertex in range(len(G))]
    else:
        return None

def min_graph_coloring(G, V) -> int:
    colors = V + 1
    assignments = []
    for i in range(V + 1, -1, -1):
        new_assignments = color(G, i)
        if new_assignments:
            colors = min(colors, i)
            assignments = new_assignments
    return colors, assignments

def main():
    K = int(input())
    pairs = [input().split() for _ in range(K)]

    # build adj-list based graph on assignments
    graph = defaultdict(set)
    for v1, v2 in pairs:
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    # min colors is realistically between 0 and V
    # could argue lower, count vertices and iterate
    V = len(set().union(*graph.values()))

    min_colors, assignments = min_graph_coloring(graph, V)
    print(min_colors)
    print(assignments)

if __name__ == "__main__":
    main()