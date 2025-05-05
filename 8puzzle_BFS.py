import heapq
import numpy as np


class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = tuple(map(tuple, initial_state))
        self.goal_state = tuple(map(tuple, goal_state))


    def manhattan_distance(self, state):
        distance = 0
        state = np.array(state)
        goal = np.array(self.goal_state)
        for i in range(1, 9):
            x1, y1 = np.where(state == i)
            x2, y2 = np.where(goal == i)
            distance += abs(x1[0] - x2[0]) + abs(y1[0] - y2[0])
        return distance


    def get_neighbors(self, state):
        neighbors = []
        state = np.array(state)
        x, y = np.where(state == 0)
        x, y = int(x[0]), int(y[0])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = state.copy()
                new_state[x, y], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[x, y]
                neighbors.append(tuple(map(tuple, new_state)))
        return neighbors


    def best_first_search(self):
        priority_queue = []
        heapq.heappush(priority_queue, (self.manhattan_distance(self.initial_state), self.initial_state, []))
        visited = set()
        while priority_queue:
            _, current_state, path = heapq.heappop(priority_queue)
            if current_state in visited:
                continue
            visited.add(current_state)
            if current_state == self.goal_state:
                return path + [current_state]
            for neighbor in self.get_neighbors(current_state):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (self.manhattan_distance(neighbor), neighbor, path + [current_state]))
        return None


def is_solvable(state):
    flat_list = [num for row in state for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                inversions += 1
    return inversions % 2 == 0


# --- USER INPUT ---
def get_state_input(name):
    print(f"\nEnter the {name} state (use 0 for the blank):")
    state = []
    for i in range(3):
        row = list(map(int, input(f"{name} Row {i+1}: ").strip().split()))
        if len(row) != 3:
            raise ValueError("Each row must have exactly 3 numbers.")
        state.append(row)
    return state


# Collect input
initial_state = get_state_input("Initial")
goal_state = get_state_input("Goal")


# Check solvability
if not is_solvable(initial_state):
    print("Initial state is not solvable.")
else:
    puzzle_solver = EightPuzzle(initial_state, goal_state)
    solution = puzzle_solver.best_first_search()


    if solution:
        print("\n8-Puzzle Solution Path:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print(np.array(state), "\n")
    else:
        print("No solution found.")

