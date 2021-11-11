# Дано целое число. Если оно является положительным, то прибавить к нему 1:
# если отрицательным, то вычесть из него 2: если нулевым, то заменить его на 10.
# Вывести полученное число.

n = input("Введите число: ")

while type(n) != int:                        # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Ввели неправильно значение")
        n = input("Введите целое число: ")

if n > 0:
    print(n + 1)
elif n < 0:
    print(n - 2)
elif n == 0:
    print(10)

