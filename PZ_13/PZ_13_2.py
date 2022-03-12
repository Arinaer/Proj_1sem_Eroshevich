# Составить генератор (yield), который выводит из строки только цифры.

def numbers(letter):
    for n in letter:
        if n.isdigit():
            yield n


print('Цифры строки: ', *list(numbers(input(f"Введите строку: "))))
