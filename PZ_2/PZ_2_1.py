#  дано трехзначное число. Используя одну операция деления нацело,
#  вывести первую цифру данного числа (сотни)

v = input("Введите число: ")
while type(v) != int:
    try:                         # обработка исключений
        v = int(v)
    except ValueError:
        print("Неправильно ввели")
        v = input("Введите целое число: ")
j = v//100
print("Первая цифра данного числа : ", j)





