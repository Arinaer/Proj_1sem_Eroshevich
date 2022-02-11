# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
# Задача из PZ_3_2.
# Даны три целых числа. Найти количество положительных  количество отрицательных чисел в исходном наборе.

from tkinter import *


def count_num(event):
    n1 = int(num1.get())
    v1 = int(num2.get())
    q1 = int(num3.get())

    k = 0
    if n1 > 0:
        k += 1
    if v1 > 0:
        k += 1
    if q1 > 0:
        k += 1

    q = 0
    if n1 < 0:
        q += 1
    if v1 < 0:
        q += 1
    if q1 < 0:
        q += 1

    positive['text'] = "Положительных", k
    negative['text'] = "Отрицательных", q


root = Tk()
root.title("Positive/negative numbers")
root.geometry('500x500')
root["bg"] = "#cdb891"

img = PhotoImage(file='heart1.jpg')
l = Label(image=img, bg="#cdb891").place(x=300, y=300)

Label(text="Введите три целых числа ", font="Arial 18", bg="#cdb891", fg="#6a5acd").place(x=100, y=50)

Label(text="Первое число: ", font="Arial 14", bg="#cdb891", fg="#6a5acd").place(x=100, y=100)
num1 = Entry(bg="#e3e2d5")
num1.place(x=250, y=100)

Label(text="Второе число: ", font="Arial 14", bg="#cdb891", fg="#6a5acd").place(x=100, y=150)
num2 = Entry(bg="#e3e2d5")
num2.place(x=250, y=150)

Label(text="Третье число: ", font="Arial 14", bg="#cdb891", fg="#6a5acd").place(x=100, y=200)
num3 = Entry(bg="#e3e2d5")
num3.place(x=250, y=200)

button1 = Button(text="Обработать", width=35, font="Arial 11", bg="#baaf96", fg="#6a5acd")
button1.place(x=100, y=250)

positive = Label(font="Arial 14", bg="#cdb891", fg="#6a5acd")
positive.place(x=100, y=300)

negative = Label(font="Arial 14", bg="#cdb891", fg="#6a5acd")
negative.place(x=100, y=350)

button1.bind('<Button-1>', count_num)

root.mainloop()
