import heapq
import networkx as nx
import matplotlib.pyplot as plt


class CitiesShortestPath:
    def __init__(self, graph, start, goal, heuristic_distances):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.heuristic = heuristic_distances


    def best_first_search(self):
        priority_queue = []
        heapq.heappush(priority_queue, (self.heuristic[self.start], self.start, 0, []))
        visited = set()


        while priority_queue:
            _, current_city, total_distance, path = heapq.heappop(priority_queue)


            if current_city in visited:
                continue
            visited.add(current_city)


            if current_city == self.goal:
                return total_distance, path + [current_city]


            for neighbor, distance in self.graph.get(current_city, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (self.heuristic[neighbor], neighbor, total_distance + distance, path + [current_city]))


        return None


def plot_graph(graph, shortest_path):
    G = nx.DiGraph()
    for city, neighbors in graph.items():
        for neighbor, distance in neighbors:
            G.add_edge(city, neighbor, weight=distance)


    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12, font_weight='bold')


    edge_labels = {(city, neighbor): f"{distance}" for city, neighbors in graph.items() for neighbor, distance in neighbors}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color='red')


    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2.5)


    plt.title("Cities Shortest Path Visualization")
    plt.show()


# ---- USER INPUT ----
def get_city_input():
    num_edges = int(input("Enter number of roads (edges): "))
    graph = {}


    print("Enter edges in format: Source Destination Distance")
    for _ in range(num_edges):
        src, dest, dist = input().strip().split()
        dist = int(dist)
        if src not in graph:
            graph[src] = []
        graph[src].append((dest, dist))


    cities = set(graph.keys())
    for neighbors in graph.values():
        for dest, _ in neighbors:
            cities.add(dest)


    heuristic = {}
    print("\nEnter heuristic values for each city:")
    for city in sorted(cities):
        h = int(input(f"Heuristic for {city}: "))
        heuristic[city] = h


    start = input("Enter start city: ").strip()
    goal = input("Enter goal city: ").strip()


    return graph, start, goal, heuristic


# Run the program
graph, start_city, goal_city, heuristic_distances = get_city_input()
solver = CitiesShortestPath(graph, start_city, goal_city, heuristic_distances)
solution = solver.best_first_search()


if solution:
    total_distance, path = solution
    print("\nShortest Path from", start_city, "to", goal_city)
    print(" -> ".join(path))
    print("Total Distance:", total_distance)
    plot_graph(graph, path)
else:
    print(" No path found!")


