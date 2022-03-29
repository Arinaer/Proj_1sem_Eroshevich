# В матрице найти минимальный элемент в предпоследнем столбце.

import random

a = int(input('Введите количество строк: '))
b = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for y in range(a)] for x in range(b)]
for i in matrix:
    print(i)

n = a-2
arr = [matrix[i][n] for i in range(len(matrix))]

print('Минимальный элемент предпоследнего столбца: ', min(arr))
