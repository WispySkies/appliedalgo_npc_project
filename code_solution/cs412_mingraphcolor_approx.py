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
    # assignments = {v: int(k) for v, k in pairs}
    colors = defaultdict()
    graph = defaultdict()
    
    for pair in pairs: # Dont want them pointing to the same memory
        v, u = pair[0], pair[1]
        colors[v], colors[u] = None, None
        
        if v not in graph:
            graph[v] = set()
            
        if u not in graph:
            graph[u] = set()
            
        graph[v].add(u)
        graph[u].add(v)
    
    print(graph)
    greedy_color(graph, colors)
    print(colors)
    

def greedy_color(graph, colors):
    
    vertexes = graph.keys()
    for u in vertexes:
        adj_colors = set()
        
        for v in graph[u]:
            if colors[v] != None:
                adj_colors.add(colors[v])
        
        for color in range(len(vertexes)):
            if color not in adj_colors:
                colors[u] = color
                break
    
if __name__ == "__main__":
    main()