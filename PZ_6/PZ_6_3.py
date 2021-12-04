# Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
# одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1).

def shift_left3(massive, shift=1):
    for i in range(shift):
        massive.insert(0, massive.pop())
    return massive


str_list = input('Введите список: ')       # Список формируется вводом его отдельных элементов через пробел.
n = str_list.split(' ')                    # строковый метод, для разделения строки в список, по указанному символу

print(shift_left3(n))
