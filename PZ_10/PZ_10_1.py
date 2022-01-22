# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого минимального элемента:
# Умножаем все элементы на минимальный элемент:

l = ['13 6 21 -36 41 -45 2 -15']
f3 = open('file_9.txt', 'w')
f3.writelines(l)
f3.close()

# Дублируем список в новый файл file_10.txt
f4 = open('file_10.txt', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

# разбиваем строку и ее значения преобразуем в числа
f3 = open('file_9.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

# Ищем минимальный элемент
f3 = open('file_9.txt')
n_list = f3.read().split()
f3.close()
n_list = list(map(int, n_list))
min_element = min(n_list)
m = n_list.index(min_element)

f4 = open('file_10.txt', 'a')    # открываем файл для дозаписи
f4.write('\n')
print('Количество элементов: ', len(k), file=f4)
f4.close()

f4 = open('file_10.txt', 'a')    # открываем файл для дозаписи
f4.write('')
print('Индекс минимального элемента: ', m, file=f4)
f4.close()

f1 = open('file_9.txt')
a = [13, 6, 21, -36, 41, -45, 2, -15]

for i in range(len(a)):
    a[i] *= m
f1.close()

f2 = open('file_10.txt', 'a')
f2.write('Элементы, умноженные минимальный элемент: ')
f2.writelines(str(a))
f2.close()
