from collections import deque


def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0:
        return False

    if m_right < 0 or c_right < 0:
        return False

    # Left side
    if m_left > 0 and c_left > m_left:
        return False

    # Right side
    if m_right > 0 and c_right > m_right:
        return False

    return True


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    # Possible boat movements
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        m_left, c_left, boat = state

        if state == goal:
            return path + [state]

        for missionaries, cannibals in moves:

            if boat == 0:
                # Boat moves from left to right
                new_m = m_left - missionaries
                new_c = c_left - cannibals
                new_boat = 1
            else:
                # Boat moves from right to left
                new_m = m_left + missionaries
                new_c = c_left + cannibals
                new_boat = 0

            new_state = (new_m, new_c, new_boat)

            if is_valid(new_m, new_c) and new_state not in visited:
                visited.add(new_state)
                queue.append(
                    (new_state, path + [state])
                )

    return None


solution = solve()

if solution:
    print("Missionaries and Cannibals Solution:\n")

    for i, state in enumerate(solution):
        m, c, boat = state

        side = "Left" if boat == 0 else "Right"

        print(
            "Step", i,
            ": Missionaries =", m,
            ", Cannibals =", c,
            ", Boat =", side
        )
else:
    print("No solution exists.")