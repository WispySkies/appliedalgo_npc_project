def generate_complete_graph(num_vertices):
    # Generate all possible combinations of vertices (edges)
    alphabet = [chr(ord('a') + i) for i in range(26)]

    formatted_edges = set()

    for v1 in alphabet[:num_vertices]:
        for v2 in alphabet[:num_vertices]:
            if v1 == v2 or f"{v1} {v2}" in formatted_edges or f"{v2} {v1}" in formatted_edges:
                continue
            formatted_edges.add(f"{v1} {v2}")

    return formatted_edges

def save_test_case(test_case, num_edges):
    filename = f"test_cases/complete_graphs/K{num_edges}_graph"
    with open(filename, 'w') as file:
        file.write(str(len(test_case)) + '\n')
        for edge in test_case:
            file.write(edge + '\n')
    print(f"Test case for {num_edges} edges saved to {filename}")

if __name__ == "__main__":
    for num_vertices in range(3, 27):
        test_case = generate_complete_graph(num_vertices)
        save_test_case(test_case, num_vertices)