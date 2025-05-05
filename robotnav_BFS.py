import heapq


class RobotNavigation:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal


    def manhattan_distance(self, pos):
        return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])


    def get_neighbors(self, pos):
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        neighbors = []
        for dx, dy in moves:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if 0 <= new_x < len(self.grid) and 0 <= new_y < len(self.grid[0]) and self.grid[new_x][new_y] == 0:
                neighbors.append((new_x, new_y))
        return neighbors


    def best_first_search(self):
        priority_queue = []
        heapq.heappush(priority_queue, (self.manhattan_distance(self.start), self.start, []))
        visited = set()


        while priority_queue:
            _, current_pos, path = heapq.heappop(priority_queue)


            if current_pos in visited:
                continue
            visited.add(current_pos)


            if current_pos == self.goal:
                return path + [current_pos]


            for neighbor in self.get_neighbors(current_pos):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (self.manhattan_distance(neighbor), neighbor, path + [current_pos]))


        return None


# ---- USER INPUT ----
def get_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the grid row by row (0=free, 1=obstacle):")
    grid = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").strip().split()))
        if len(row) != cols:
            raise ValueError("Each row must contain exactly {} values.".format(cols))
        grid.append(row)


    start = tuple(map(int, input("Enter start position (row col): ").strip().split()))
    goal = tuple(map(int, input("Enter goal position (row col): ").strip().split()))
    return grid, start, goal


# Run with input
grid, start, goal = get_input()
robot_solver = RobotNavigation(grid, start, goal)
robot_solution = robot_solver.best_first_search()


# Output
if robot_solution:
    print("\n Robot Navigation Path (from start to goal):")
    for step, pos in enumerate(robot_solution):
        print(f"Step {step}: Move to {pos}")
else:
    print(" No path found!")

