from collections import deque

def get_neighbors(state):
    neighbors = []

    index = state.index(0)
    row = index // 3
    col = index % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col

            new_state = list(state)
            new_state[index], new_state[new_index] = \
                new_state[new_index], new_state[index]

            neighbors.append(tuple(new_state))

    return neighbors


def solve_8_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [state]))

    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = solve_8_puzzle(start, goal)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):
        print("Step", step)
        print_state(state)
else:
    print("No solution exists.")