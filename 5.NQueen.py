import random


N = 8
POP_SIZE = 20
GENERATIONS = 1000
MUTATION_RATE = 0.8


# 1. Random board বানায়
def create_board():

    board = []

    for i in range(N):

        number = random.randint(0, N - 1)

        board.append(number)

    return board


# 2. Fitness বের করে
# Fitness = 2 * row conflicts + 3 * diagonal conflicts
def fitness(board):

    row_conflicts = 0
    diagonal_conflicts = 0

    for i in range(N):

        for j in range(i + 1, N):

            # একই row
            if board[i] == board[j]:

                row_conflicts += 1

            # একই diagonal
            elif abs(board[i] - board[j]) == abs(i - j):

                diagonal_conflicts += 1


    total_fitness = 2 * row_conflicts + 3 * diagonal_conflicts

    return total_fitness


# 3. দুই parent থেকে child বানায়
# Crossover point = 3
def crossover(parent1, parent2):

    crossover_point = 3


    child1 = parent1[:crossover_point] + parent2[crossover_point:]

    child2 = parent2[:crossover_point] + parent1[crossover_point:]


    return child1, child2


# 4. Inversion Mutation
# Random একটি অংশ select করে reverse করে
def mutate(board):

    new_board = board[:]


    # প্রথম random position
    start = random.randint(0, N - 2)

    # দ্বিতীয় random position
    end = random.randint(start + 1, N - 1)


    # selected অংশ reverse করা
    selected_part = new_board[start:end + 1]

    selected_part.reverse()

    new_board[start:end + 1] = selected_part


    return new_board


# 5. Genetic Algorithm
def genetic_algorithm():

    # প্রথমে 20টা random board
    population = []


    for i in range(POP_SIZE):

        board = create_board()

        population.append(board)


    # Generation শুরু
    for generation in range(GENERATIONS):


        # Fitness অনুযায়ী board সাজানো
        population.sort(key=fitness)


        # সবচেয়ে ভালো board
        best_board = population[0]


        # যদি fitness 0 হয়
        if fitness(best_board) == 0:

            print("Solution found!")

            print("Generation:", generation)

            return best_board


        # প্রথম 10টা ভালো board parent
        parents = population[:POP_SIZE // 2]


        # নতুন children
        children = []


        # 20টা child বানানো
        while len(children) < POP_SIZE:


            # random দুইটা parent
            parent1 = random.choice(parents)

            parent2 = random.choice(parents)


            # crossover
            child1, child2 = crossover(parent1, parent2)


            # Child 1 mutation
            random_number = random.random()

            if random_number < MUTATION_RATE:

                child1 = mutate(child1)


            # Child 2 mutation
            random_number = random.random()

            if random_number < MUTATION_RATE:

                child2 = mutate(child2)


            # children list-এ যোগ
            children.append(child1)

            children.append(child2)


        # পুরোনো population + নতুন children
        population = population + children


        # আবার fitness অনুযায়ী সাজানো
        population.sort(key=fitness)


        # সেরা 20টা রাখা
        population = population[:POP_SIZE]


    # 1000 generation শেষ হয়ে গেলে
    print("No solution found.")


    return population[0]


# Program শুরু
result = genetic_algorithm()


print("Final board:")

print(result)


print("Fitness:", fitness(result))