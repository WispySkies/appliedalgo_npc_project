"""
CS412 Applied Algorithms

Welsh-Powell Coloring Algorithm

Declan McCue - Conor McFadden

Heavily based on https://www.geeksforgeeks.org/welsh-powell-graph-colouring-algorithm/
"""

from collections import defaultdict

class Graph:
    def __init__(self, edges):
        
        # build adj-list based graph on assignments
        self.graph = defaultdict(set)
        for v1, v2 in edges:
            self.graph[v1].add(v2)
            self.graph[v2].add(v1)

        # unpack all vals into an iterable, set union for dups, get length for count
        self.vertex_count = len(set().union(*self.graph.keys()))
    
    def welshpowell(self):
        # build degrees by (label, degree)
        degrees = [(vertex_label, len(self.graph[vertex_label])) for vertex_label in self.graph]

        # sort degrees by degree, high low
        degrees.sort(key=lambda x: x[1], reverse=True)

        colors = {vertex_label: -1 for vertex_label in self.graph}

        colors[degrees.pop()[0]] = 0
        next_color = 1

        # keep coloring vertices until all are covered
        while degrees:
            vertex, _ = degrees.pop()

            # uncolored, we color it then increase
            if colors[vertex] == -1:
                colors[vertex] = next_color
            next_color += 1
            
            # if prior, color new neighbors with the +1
            # find vertex's neighbors and color them with new color if != -1
            for neighbor in self.graph[vertex]:
                if colors[neighbor] != -1:
                    colors[neighbor] = next_color

            # edge case, no vertices means we can color it 0 :)
            if not self.graph[vertex]:
                colors[vertex] = 0

        return next_color

def main():
    K = int(input())
    pairs = [input().split() for _ in range(K)]

    graph = Graph(pairs)
    print(graph.welshpowell())

if __name__ == "__main__":
    main()