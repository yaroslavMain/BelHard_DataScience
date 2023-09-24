from random import randint

N = 3
M = 3

matrix = [[randint(1, 10) for _ in range(N)] for _ in range(M)]

print(matrix)

for i in range(0, N, 1):
    for j in range(0, M, 1):
        if matrix[i][j] % 2 == 0:
            matrix[i][j] = 0
print(matrix)
