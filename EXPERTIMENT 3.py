from collections import deque


def water_jug(capacity1, capacity2, target):
    start = (0, 0)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (jug1, jug2), path = queue.popleft()

        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]

        next_states = [
            (capacity1, jug2),  # Fill Jug 1
            (jug1, capacity2),  # Fill Jug 2
            (0, jug2),          # Empty Jug 1
            (jug1, 0),          # Empty Jug 2
        ]

        # Pour Jug 1 -> Jug 2
        amount = min(jug1, capacity2 - jug2)
        next_states.append((jug1 - amount, jug2 + amount))

        # Pour Jug 2 -> Jug 1
        amount = min(jug2, capacity1 - jug1)
        next_states.append((jug1 + amount, jug2 - amount))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(jug1, jug2)]))

    return None


capacity1 = 4
capacity2 = 3
target = 2

solution = water_jug(capacity1, capacity2, target)

if solution:
    print("Water Jug Solution:")
    for step, state in enumerate(solution):
        print("Step", step, ":", state)

    print("\nGoal reached!")
else:
    print("No solution exists.")