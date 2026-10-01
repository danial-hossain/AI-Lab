import random


N = 8
POP_SIZE = 15
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
# Row conflict = +1
# Diagonal conflict = +2
def fitness(board):

    fitness_score = 0

    for i in range(N):

        for j in range(i + 1, N):

            # একই row
            if board[i] == board[j]:

                fitness_score += 1

            # একই diagonal
            elif abs(board[i] - board[j]) == abs(i - j):

                fitness_score += 2


    return fitness_score


# 3. Crossover
# Crossover point = 4
def crossover(parent1, parent2):

    crossover_point = 4

    child1 = parent1[:crossover_point] + parent2[crossover_point:]

    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2


# 4. Scramble Mutation
def mutate(board):

    new_board = board[:]

    # প্রথম position
    start = random.randint(0, N - 2)

    # দ্বিতীয় position
    end = random.randint(start + 1, N - 1)

    # selected অংশ
    selected_part = new_board[start:end + 1]

    # selected অংশ randomভাবে shuffle
    random.shuffle(selected_part)

    # board-এ আবার বসানো
    new_board[start:end + 1] = selected_part

    return new_board


# 5. Genetic Algorithm
def genetic_algorithm():

    # প্রথমে 15টা random board
    population = []

    for i in range(POP_SIZE):

        board = create_board()

        population.append(board)


    # Generation
    for generation in range(GENERATIONS):

        # Fitness কম থেকে বেশি
        population.sort(key=fitness)

        # সবচেয়ে ভালো board
        best_board = population[0]


        # Fitness 0 হলে perfect solution
        if fitness(best_board) == 0:

            print("Solution found!")

            print("Generation:", generation)

            return best_board


        # প্রথম অর্ধেক ভালো board parent
        parents = population[:POP_SIZE // 2]

        children = []


        # নতুন child বানানো
        while len(children) < POP_SIZE:

            # random দুই parent
            parent1 = random.choice(parents)

            parent2 = random.choice(parents)


            # Crossover
            child1, child2 = crossover(parent1, parent2)


            # Child 1 mutation
            random_number = random.random()

            if random_number < MUTATION_RATE:

                child1 = mutate(child1)


            # Child 2 mutation
            random_number = random.random()

            if random_number < MUTATION_RATE:

                child2 = mutate(child2)


            # Children list-এ যোগ
            children.append(child1)

            children.append(child2)


        # Old population + new children
        population = population + children


        # আবার fitness অনুযায়ী সাজানো
        population.sort(key=fitness)


        # সেরা 15টা রাখা
        population = population[:POP_SIZE]


    print("No solution found.")

    return population[0]


# Program শুরু
result = genetic_algorithm()


print("Final board:")

print(result)


print("Fitness:", fitness(result))