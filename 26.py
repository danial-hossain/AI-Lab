# 1. Mother facts
mother = [
    ('M01', 'Ch01'),
    ('M01', 'Ch02')
]


# 2. Father facts
father = [
    ('F01', 'Ch02'),
    ('F01', 'Ch03')
]


# 3. Male persons
male = [
    'F01',
    'Ch01'
]


# X-এর mother খুঁজে বের করবে
def find_mother(X):

    for i in range(len(mother)):

        if mother[i][1] == X:

            return mother[i][0]

    return None


# X-এর father খুঁজে বের করবে
def find_father(X):

    for i in range(len(father)):

        if father[i][1] == X:

            return father[i][0]

    return None


# X-এর brothers খুঁজে বের করবে
def find_brothers(X):

    brothers = []


    # -------- Mother দিয়ে brother খুঁজি --------

    m = find_mother(X)

    for i in range(len(mother)):

        if mother[i][0] == m:

            person = mother[i][1]

            if person != X and person in male:

                brothers.append(person)


    # -------- Father দিয়ে brother খুঁজি --------

    f = find_father(X)

    for i in range(len(father)):

        if father[i][0] == f:

            person = father[i][1]

            if person != X and person in male:

                brothers.append(person)


    return brothers


# Main
X = input("Person: ")

print("Brothers:", find_brothers(X))