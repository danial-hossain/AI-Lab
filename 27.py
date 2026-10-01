# Goal state
goal = [
    (1, 0, 0),
    (2, 0, 1),
    (3, 0, 2),
    (4, 1, 0),
    (5, 1, 1),
    (6, 1, 2),
    (7, 2, 0),
    (8, 2, 1)
]


# Current state
current = [
    (1, 0, 0),
    (2, 0, 1),
    (3, 0, 2),
    (4, 1, 0),
    (5, 2, 1),
    (6, 1, 2),
    (7, 2, 0),
    (8, 2, 2)
]


def heuristic():

    distance = 0

    for i in range(8):

        tile = current[i][0]

        current_row = current[i][1]
        current_col = current[i][2]

        goal_row = goal[i][1]
        goal_col = goal[i][2]

        distance = distance + abs(current_row - goal_row)
        distance = distance + abs(current_col - goal_col)

    return distance


answer = heuristic()

print("Heuristic:", answer)