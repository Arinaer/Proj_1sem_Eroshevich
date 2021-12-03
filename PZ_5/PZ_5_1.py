# С помощью функций получить вертикальную и горизонтальную линии. Линия проводится
# многократной печатью символа. Заключить слово в рамку из полученных линий.


def gorizontal_line(length):   # функция для вывода горизонтальной линии на экран.
    while length > 0:
        print('-', end='')
        length -= 1
    print()


def vertical_line(height, length, text):   # функция для вывода вертикальной линии на экран.
    mid = height // 2 + 1   # определение средней линии.
    while height > 0:
        if height != mid:   # если линия не средняя, то печатаем пустую строку.
            print('|', ' '*(length-2), '|', sep='')
        else:               # если линия средняя, то будет вызвана функция форматированной печати текста.
            print('|', print_text(text, length-2), '|', sep='')

        height -= 1


def print_text(text, length):     # форматированная печать текста.
    return "{:^{i}}".format(text, i=length)


def main(height, length, text):   # запуск приложения.
    gorizontal_line(length)
    vertical_line(height, length, text)
    gorizontal_line(length)


main(5, 30, 'hello')
