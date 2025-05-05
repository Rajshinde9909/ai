def solve_crossword(grid_str, words):
    grid = [list(row.strip()) for row in grid_str.split('\n') if row.strip()]
    height, width = len(grid), len(grid[0]) if grid else 0


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
        else:
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
        else:
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


if __name__ == "__main__":
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

