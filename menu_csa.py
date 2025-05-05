import itertools
import matplotlib.pyplot as plt
import networkx as nx


def solve_cryptarithmetic(words, result):
    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        print("Too many unique letters, cannot solve.")
        return None
    unique_chars = list(unique_chars)
    
    for perm in itertools.permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue
        words_nums = [sum(mapping[char] * (10 ** i) for i, char in enumerate(word[::-1])) for word in words]
        result_num = sum(mapping[char] * (10 ** i) for i, char in enumerate(result[::-1]))
        if sum(words_nums) == result_num:
            print("\nSolution Found!")
            for char, num in mapping.items():
                print(f"{char} = {num}")
            return mapping
    print("\nNo solution found.")
    return None


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


def solve_crossword(grid_str, words):
    grid = [list(row.strip()) for row in grid_str.split('\n') if row.strip()]
    height, width = len(grid), len(grid[0]) if grid else 0


    # Find slots (horizontal and vertical)
    slots = []
    for i in range(height):
        j = 0
        while j < width:
            if grid[i][j] == '.':
                start = j
                while j < width and grid[i][j] == '.':
                    j += 1
                if j - start > 1:
                    slots.append(('across', i, start, j - start))
            else:
                j += 1
    for j in range(width):
        i = 0
        while i < height:
            if grid[i][j] == '.':
                start = i
                while i < height and grid[i][j] == '.':
                    i += 1
                if i - start > 1:
                    slots.append(('down', start, j, i - start))
            else:
                i += 1


    def can_place(word, slot, current_grid):
        direction, row, col, length = slot
        if len(word) != length:
            return False
        if direction == 'across':
            for k, char in enumerate(word):
                if current_grid[row][col + k] not in ('.', char):
                    return False
        else:  # down
            for k, char in enumerate(word):
                if current_grid[row + k][col] not in ('.', char):
                    return False
        return True


    def place_word(word, slot, current_grid):
        direction, row, col, length = slot
        new_grid = [r[:] for r in current_grid]
        if direction == 'across':
            for k, char in enumerate(word):
                new_grid[row][col + k] = char
        else:  # down
            for k, char in enumerate(word):
                new_grid[row + k][col] = char
        return new_grid


    def backtrack(grid, slots, words, used):
        if not slots:
            return grid
        slot = slots[0]
        for i, word in enumerate(words):
            if not used[i] and can_place(word, slot, grid):
                used[i] = True
                new_grid = place_word(word, slot, grid)
                result = backtrack(new_grid, slots[1:], words, used)
                if result:
                    return result
                used[i] = False
        return None


    used = [False] * len(words)
    solution = backtrack(grid, slots, words, used)
    if solution:
        return '\n'.join(''.join(row) for row in solution)
    return None


def main():
    while True:
        print("\nConstraint Satisfaction Problem Solver")
        print("1. Solve Cryptarithmetic Puzzle")
        print("2. Solve Map Coloring Problem")
        print("3. Solve Crossword Puzzle")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            words = input("Enter words (comma-separated): ").split(",")
            result = input("Enter result word: ")
            solve_cryptarithmetic(words, result)
        elif choice == '2':
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
        elif choice == '3':
            print("Enter the crossword grid (# for blocks, . for empty spaces, one row per line). Type 'done' when finished:")
            grid_lines = []
            while True:
                line = input()
                if line == "done":
                    break
                grid_lines.append(line)
            grid = '\n'.join(grid_lines)
            words = input("Enter words to place (comma-separated): ").split(",")
            solution = solve_crossword(grid, words)
            if solution:
                print("\nCrossword Solution:")
                print(solution)
            else:
                print("\nNo solution found.")
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

