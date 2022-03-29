# Для каждого столбца матрицы с четным номером найти сумму ее элементов.

import random


def func1(list):
    sum = 0
    for i in list:
        sum += i
    return sum


a = 9
b = 3

matrix = [[random.randint(1, 10) for y in range(a)] for x in range(b)]
matrix_reversed = [[0 for y in range(b)] for x in range(a)]
for i in matrix:
    print(i)
    print("\n")

print('Столбцы матрицы: ')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix_reversed[j][i] = matrix[i][j]
for i in matrix_reversed:
    print(i)


print('\n', 'Четные столбцы матрицы: ')
arr = []
for i in range(len(matrix_reversed)):
    if i % 2 == 0:
        print(matrix_reversed[i])
        arr.append(func1(matrix_reversed[i]))

print("\n")
print('Сумма элементов: ', arr)
