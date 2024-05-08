import cs412_mingraphcolor_approx
import cs412_mingraphcolor_exact
import random

def generate_test_case(num_nodes, avg_degree):
    edges = set()

    # create cliques
    for i in range(1, num_nodes + 1):
        for j in range(i + 1, min(i + avg_degree, num_nodes) + 1):
            edges.add((i, j))

    # increase density
    while len(edges) < num_nodes * avg_degree:
        node1 = random.randint(1, num_nodes)
        node2 = random.randint(1, num_nodes)
        if node1 != node2:
            edges.add((node1, node2))

    return edges

def write_test_case(filename, edges):
    with open(filename, 'w') as f:
        f.write(f"{len(edges)}\n")
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")

def test_case(edges) -> bool:
    exact = cs412_mingraphcolor_exact.get_min(edges)
    print("exact", exact)
    approx = cs412_mingraphcolor_approx.get_min(edges)
    print("approx", approx)
    return exact != approx

def main():
    for n_nodes in range(100, 450):
        print(f"try node {n_nodes}")
        rand_deg = random.randint(3, n_nodes)
        edges = generate_test_case(n_nodes, rand_deg)

        if test_case(edges):
            print(f"Test passed. {n_nodes} {rand_deg}")
            write_test_case(f"rand_tests/test_case{n_nodes}_{rand_deg}.txt", edges)

if __name__ == "__main__":
    main()