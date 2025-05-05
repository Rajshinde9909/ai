import matplotlib.pyplot as plt
import networkx as nx


def solve_map_coloring(graph, colors):
    color_map = {}
    def is_valid(node, color):
        return all(color_map.get(neigh) != color for neigh in graph[node])
    def backtrack(node_index):
        if node_index == len(graph):
            return True
        node = list(graph.keys())[node_index]
        for color in colors:
            if is_valid(node, color):
                color_map[node] = color
                if backtrack(node_index + 1):
                    return True
                del color_map[node]
        return False
    if backtrack(0):
        return color_map
    return None


def draw_colored_map(graph, color_map):
    G = nx.Graph()
    for node in graph:
        G.add_node(node)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)


    pos = nx.spring_layout(G)
    node_colors = [color_map[node].strip().lower() for node in G.nodes()]


    plt.figure(figsize=(6, 6))
    nx.draw(G, pos,
            node_color=node_colors,
            with_labels=True,
            node_size=1000,
            font_size=12,
            font_weight='bold')
    plt.title("Map Coloring Solution")
    plt.show()


if __name__ == "__main__":
    num_regions = int(input("Enter number of regions: "))
    graph = {}
    print("Enter adjacency list (format: region neighbors1 neighbors2 ...). Type 'done' to finish:")
    while True:
        line = input()
        if line == "done":
            break
        parts = line.split()
        graph[parts[0]] = parts[1:]
    colors = input("Enter colors available (comma-separated): ").split(",")
    solution = solve_map_coloring(graph, colors)
    if solution:
        print("\nMap Coloring Solution:")
        for region, color in solution.items():
            print(f"{region} -> {color}")
        draw_colored_map(graph, solution)
    else:
        print("\nNo solution found.")


