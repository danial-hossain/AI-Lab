

def heuristic(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    # Up
    if row > 0:
        new_state = state.copy()
        new_zero = zero - 3
        new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
        neighbors.append(new_state)

    # Down
    if row < 2:
        new_state = state.copy()
        new_zero = zero + 3
        new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
        neighbors.append(new_state)

    # Left
    if col > 0:
        new_state = state.copy()
        new_zero = zero - 1
        new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
        neighbors.append(new_state)

    # Right
    if col < 2:
        new_state = state.copy()
        new_zero = zero + 1
        new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
        neighbors.append(new_state)

    return neighbors


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def hill_climbing(start, goal):

    current = start
    step = 0

    while True:

        print("Step:", step)
        print_board(current)
        print("Heuristic:", heuristic(current, goal))

        # Goal check
        if current == goal:
            print("Goal reached!")
            return

        # Get all possible next states
        neighbors = get_neighbors(current)

        # Find the best neighbor
        best = current

        for state in neighbors:
            if heuristic(state, goal) < heuristic(best, goal):
                best = state

        # No better neighbor
        if best == current:
            print("No better state found.")
            print("Hill climbing stopped.")
            return

        current = best
        step += 1


# Starting puzzle
start = [
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
]

# Target puzzle
goal = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]

hill_climbing(start, goal)