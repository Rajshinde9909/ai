def dfs_water_jug(cap_a, cap_b, target):
    from collections import deque
 
    def is_valid(state):
        return 0 <= state[0] <= cap_a and 0 <= state[1] <= cap_b
 
    def next_states(state):
        a, b = state
        return [
            (cap_a, b),  # Fill Jug A
            (a, cap_b),  # Fill Jug B
            (0, b),      # Empty Jug A
            (a, 0),      # Empty Jug B
            (a - min(a, cap_b - b), b + min(a, cap_b - b)),  # Pour A -> B
            (a + min(b, cap_a - a), b - min(b, cap_a - a))   # Pour B -> A
        ]
 
    stack = deque([(0, 0)])
    visited = set()
 
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
 
        a, b = current
        print(f"Visiting state: {current}")
 
        if a == target or b == target:
            print(f"Solution found: {current}")
            return
 
        for state in next_states(current):
            if is_valid(state) and state not in visited:
                stack.append(state)
 
    print("No solution found.")
 
# Sample Input for DFS
cap_a = int(input("Enter capacity of Jug A: "))
cap_b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))
dfs_water_jug(cap_a, cap_b, target)

