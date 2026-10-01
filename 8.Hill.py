def heuristic(state, goal):

    distance = 0

    # 1 থেকে 8 পর্যন্ত tile
    for tile in range(1, 9):

        # current state-এ tile কোথায় আছে
        current_pos = state.index(tile)

        # goal state-এ tile কোথায় আছে
        goal_pos = goal.index(tile)

        # current row, column
        current_row = current_pos // 3
        current_col = current_pos % 3

        # goal row, column
        goal_row = goal_pos // 3
        goal_col = goal_pos % 3

        # Manhattan Distance
        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3


    # Up
    if row > 0:

        new_state = state.copy()

        new_zero = zero - 3

        new_state[zero], new_state[new_zero] = \
            new_state[new_zero], new_state[zero]

        neighbors.append(new_state)


    # Down
    if row < 2:

        new_state = state.copy()

        new_zero = zero + 3

        new_state[zero], new_state[new_zero] = \
            new_state[new_zero], new_state[zero]

        neighbors.append(new_state)


    # Left
    if col > 0:

        new_state = state.copy()

        new_zero = zero - 1

        new_state[zero], new_state[new_zero] = \
            new_state[new_zero], new_state[zero]

        neighbors.append(new_state)


    # Right
    if col < 2:

        new_state = state.copy()

        new_zero = zero + 1

        new_state[zero], new_state[new_zero] = \
            new_state[new_zero], new_state[zero]

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


        # প্রশ্নে successors print করতে বলেছে
        print("Successors:")

        for state in neighbors:

            print_board(state)

            print("Heuristic:", heuristic(state, goal))


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


# Current state
start = [
    8, 1, 2,
    3, 6, 4,
    0, 7, 5
]


# Goal state
goal = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
]


hill_climbing(start, goal)