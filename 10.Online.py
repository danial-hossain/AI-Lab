def rotate(matrix, n):

    result = []

    for i in range(n):

        row = []

        for j in range(n):

            row.append(matrix[j][n - 1 - i])

        result.append(row)

    return result


n = int(input())

matrix = []

for i in range(n):
    matrix.append(input().split())

answer = rotate(matrix, n)

for i in range(n):
    print(*answer[i])