"""
CS412 Applied Algorithms

Decision-based Minimum Graph Coloring

Declan McCue - Conor McFadden

Heavily based on https://www.geeksforgeeks.org/m-coloring-problem/
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
        self.vertex_count = len(set().union(*self.graph.values()))

    def can_color(self, vertex, used_colors, target_color):

        # check all neighbors of vertex and make sure the colors not used
        for neighbor in self.graph[vertex]:
            if used_colors[neighbor] == target_color:
                return False
        
        return True
    
    def color_recursive(self, vertices, vertex, result):
        if vertex == self.vertex_count:
            return True
        
        for proposed_color in range(self.vertex_count):
            if self.can_color(vertices[vertex], result, proposed_color):
                result[vertices[vertex]] = proposed_color

                if self.color_recursive(vertices, vertex + 1, result):
                    return True
                
                result[vertices[vertex]] = -1
    
    def brute_force_color(self):
        vertices = list(self.graph.keys())
        result = {vertex: -1 for vertex in vertices}

        if not self.color_recursive(vertices, 0, result):
            print("No solution exists.")
            return None
        
        max_color = max(result.values()) + 1
        return result, max_color

def get_min(edges):
    K = len(edges)
    pairs = [(u, v) for u, v in edges]

    graph = Graph(pairs)
    _, max_color = graph.brute_force_color()
    return max_color

def main():
    K = int(input())
    pairs = [input().split() for _ in range(K)]

    graph = Graph(pairs)
    colors, n_colors = graph.brute_force_color()

    if colors:
        print(n_colors)
        for vertex, color in colors.items():
            print(vertex, color)

if __name__ == "__main__":
    main()
