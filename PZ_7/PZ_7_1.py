# Дана строка. Подсчитать количество содержащихся в ней прописных латинских букв.

s = "НиЖниЙ рЕгисТР!"
print(f'Кол-во прописных букв: {sum(map(str.islower, s))}')
