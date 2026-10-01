import random

N = 8
POP_SIZE = 10
GENERATIONS = 1000
MUTATION_RATE = 0.8


# 1. Random board বানায়
def create_board():
    board = []

    for i in range(N):
        number = random.randint(0, N - 1)
        board.append(number)

    return board


# 2. কয়টা conflict আছে সেটা বের করে
def fitness(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            # একই row
            if board[i] == board[j]:
                conflicts += 1

            # একই diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# 3. দুই parent থেকে child বানায়
def crossover(parent1, parent2):

    middle = N // 2

    child1 = parent1[:middle] + parent2[middle:]
    child2 = parent2[:middle] + parent1[middle:]

    return child1, child2


# 4. Child-এর কিছু position random করে
def mutate(board):

    new_board = board[:]

    times = random.randint(1, 2)

    for i in range(times):

        column = random.randint(0, N - 1)
        row = random.randint(0, N - 1)

        new_board[column] = row

    return new_board


# 5. Genetic Algorithm
def genetic_algorithm():

    # প্রথমে 10টা random board
    population = []

    for i in range(POP_SIZE):
        board = create_board()
        population.append(board)


    for generation in range(GENERATIONS):

        # fitness অনুযায়ী board সাজানো
        population.sort(key=fitness)


        # সবচেয়ে ভালো board
        best_board = population[0]


        # যদি conflict 0 হয়
        if fitness(best_board) == 0:

            print("Solution found!")
            print("Generation:", generation)

            return best_board


        # প্রথম 5টা ভালো board parent
        parents = population[:POP_SIZE // 2]

        children = []

        # নতুন child বানানো
        while len(children) < POP_SIZE // 2:

            parent1 = random.choice(parents)
            parent2 = random.choice(parents)


            child1, child2 = crossover(parent1, parent2)


            # mutation
            random_number = random.random()

            if random_number < MUTATION_RATE:
                child1 = mutate(child1)


            random_number = random.random()

            if random_number < MUTATION_RATE:
                child2 = mutate(child2)


            children.append(child1)
            children.append(child2)


        # পুরোনো population + নতুন children
        population = population + children


        # আবার fitness অনুযায়ী সাজাই
        population.sort(key=fitness)


        # সেরা 10টা রাখি
        population = population[:POP_SIZE]


    print("No solution found.")

    return population[0]


# Program শুরু
result = genetic_algorithm()

print("Final board:")
print(result)

print("Fitness:", fitness(result))