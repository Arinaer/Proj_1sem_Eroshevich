# Выполнить сортировку словаря d = {'a': 1, 'b': 2, 'c': 3}
# (Наоборот)

di = {'a': 1, 'b': 2, 'c': 3}
print('Исходный словарь: ', di)
di = dict(sorted(di.items(), reverse=True))
print('Перевернутый: ', di)
