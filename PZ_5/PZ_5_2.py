# Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг: значение A
# переходит в C, значение C — в B, значение B — в A (A, B, C — вещественные
# параметры, являющиеся одновременно входными и выходными). С помощью этой функции
# выполнить левый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1)
# и (A2, B2, C2).

def shift_left3(shift=2):
    massive = [a, b, c]
    for i in range(shift):
        massive.insert(0, massive.pop())
    return massive


a = (input("Введите число: "))
b = (input("Введите число: "))
c = (input("Введите число: "))

while type(a) != float:                      # Обработка исключений.
    try:
        a = float(a)
    except ValueError:
        print("Ввели неправильное значение")
        a = input("Введите еще раз: ")

while type(b) != float:                      # Обработка исключений.
    try:
        b = float(b)
    except ValueError:
        print("Ввели неправильное значение")
        b = input("Введите еще раз: ")

while type(c) != float:                      # Обработка исключений.
    try:
        c = float(c)
    except ValueError:
        print("Ввели неправильное значение")
        c = input("Введите еще раз: ")

print(shift_left3())