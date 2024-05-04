import random

# same as complete_graph_generator, but sample some edges so it's not fully complete

def generate_extended_alphabet(num_letters):
    if num_letters == 1:
        return [chr(ord('a') + i) for i in range(26)]
    else:
        prev_combinations = generate_extended_alphabet(num_letters - 1)
        extended_alphabet = [prev + chr(ord('a') + i) for prev in prev_combinations for i in range(26)]
        return extended_alphabet

def generate_complete_graph(num_vertices):
    # Generate all possible combinations of vertices (edges)
    extended_alphabet = generate_extended_alphabet(3)
    formatted_edges = set()

    for v1 in extended_alphabet[:num_vertices]:
        for v2 in extended_alphabet[:num_vertices]:
            if v1 == v2 or f"{v1} {v2}" in formatted_edges or f"{v2} {v1}" in formatted_edges:
                continue
            formatted_edges.add(f"{v1} {v2}")

    return formatted_edges
    # return random.sample(formatted_edges, int(0.5 * len(formatted_edges)))

def save_test_case(test_case, num_edges):
    filename = f"test_cases/random_graphs/{num_edges}_rand_graph"
    with open(filename, 'w') as file:
        file.write(str(len(test_case)) + '\n')
        for edge in test_case:
            file.write(edge + '\n')
    print(f"Test case for {num_edges} edges saved to {filename}")

if __name__ == "__main__":
    for num_vertices in range(100, 1000, 10):
        test_case = generate_complete_graph(num_vertices)
        save_test_case(test_case, num_vertices)