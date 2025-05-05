import numpy as np


class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = np.array(initial_state)
        self.goal_state = np.array(goal_state)


    def manhattan_distance(self, state):
        distance = 0
        for i in range(1, 9):
            x1, y1 = np.where(state == i)
            x2, y2 = np.where(self.goal_state == i)
            distance += abs(x1[0] - x2[0]) + abs(y1[0] - y2[0])
        return distance


    def get_neighbors(self, state):
        neighbors = []
        x, y = np.where(state == 0)
        x, y = int(x[0]), int(y[0])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = state.copy()
                new_state[x, y], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[x, y]
                neighbors.append(new_state)


        return neighbors


    def hill_climbing(self):
        current_state = self.initial_state.copy()
        current_heuristic = self.manhattan_distance(current_state)


        print("\nInitial State:")
        print(current_state, "\n")


        steps = 0
        while True:
            neighbors = self.get_neighbors(current_state)
            next_state = None
            next_heuristic = current_heuristic


            for neighbor in neighbors:
                h = self.manhattan_distance(neighbor)
                if h < next_heuristic:
                    next_state = neighbor
                    next_heuristic = h


            if next_state is None or next_heuristic >= current_heuristic:
                print("Final State (Local Minimum or Goal Reached):")
                print(current_state, "\n")
                return current_state


            current_state = next_state
            current_heuristic = next_heuristic
            steps += 1


            print(f"Step {steps}:")
            print(current_state, "\n")


# Function to get a 3x3 puzzle state from user
def get_user_input(name):
    print(f"Enter the {name} state (row by row, use 0 for blank):")
    state = []
    for i in range(3):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1} (e.g., 1 2 3): ").strip().split()))
                if len(row) != 3 or any(n < 0 or n > 8 for n in row):
                    raise ValueError
                state.append(row)
                break
            except ValueError:
                print("Invalid input. Enter 3 integers between 0 and 8 (inclusive), separated by spaces.")
    return state


# Get user input
initial_state = get_user_input("initial")
goal_state = get_user_input("goal")


# Run the puzzle
puzzle = EightPuzzle(initial_state, goal_state)
result = puzzle.hill_climbing()