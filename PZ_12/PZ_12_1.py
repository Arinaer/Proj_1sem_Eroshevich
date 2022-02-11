# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1). (Вариант 14: https://i.stack.imgur.com/5MatP.png)

from tkinter import*
from tkinter.ttk import Combobox
from tkinter.ttk import Spinbox

root = Tk()
root.title("Step 3 Registration")
root.geometry('800x600')
root["bg"] = "SteelBlue4"

frame1 = Frame(root, highlightbackground="White", bg="SteelBlue4", highlightthickness=5, width=600, height=550, bd=0)
frame1.pack()

Label(text="Step 3 Registration details: ", font="Times 16", bg="SteelBlue4", fg="white").place(x=300, y=10)
Label(text="University: ", font="Times 14", bg="SteelBlue4", fg="white").place(x=200, y=100)
Label(text="Institute: ", font="Times 14", bg="SteelBlue4", fg="white").place(x=200, y=150)
Label(text="Branch: ", font="Times 14", bg="SteelBlue4", fg="white").place(x=200, y=200)
Label(text="Degree: ", font="Times 14", bg="SteelBlue4", fg="white").place(x=200, y=250)
Label(text="Pursuing ", font="Times 14", bg="SteelBlue4", fg="white").place(x=450, y=250)
Label(text="Completed ", font="Times 14", bg="SteelBlue4", fg="white").place(x=560, y=250)
Label(text="Avarage CPI: ", font="Times 14", bg="SteelBlue4", fg="white").place(x=200, y=300)
Label(text="Upto", font="Times 14", bg="SteelBlue4", fg="white").place(x=370, y=300)
Label(text="Th Semester", font="Times 14", bg="SteelBlue4", fg="white").place(x=480, y=300)
Label(text="Experience: ", font="Times 14", bg="SteelBlue4", fg="white").place(x=200, y=350)
Label(text="Years", font="Times 14", bg="SteelBlue4", fg="white").place(x=380, y=350)
Label(text="Your Website or Blog: ", font="Times 14", bg="SteelBlue4", fg="white").place(x=200, y=400)

txt1 = Entry(width=50)    # Кнопка University
txt1.place(x=300, y=100)

txt2 = Entry(width=50)    # Кнопка Institute
txt2.place(x=300, y=150)

txt3 = Entry(width=50)    # Кнопка Website or Blog
txt3.place(x=380, y=403)

list1 = Combobox(height=3, width=20, font=("Times", 12), background="SteelBlue4")   # Branch
list1['values'] = ("--select--", "Rostov", "Azov", "Taganrog")
list1.current(0)
list1.place(x=300, y=200)

list2 = Combobox(height=3, width=10, font=("Times", 12), background="SteelBlue4")   # Degree
list2['values'] = ("--select--", "I", "II", "III", "IV")
list2.current(0)
list2.place(x=300, y=250)

ch = Checkbutton(bg="SteelBlue4", activebackground="SteelBlue4")   # Кнопка Pursuing
ch.place(x=425, y=250)
ch = Checkbutton(bg="SteelBlue4", activebackground="SteelBlue4")   # Кнопка Completed
ch.place(x=535, y=250)

spin1 = Spinbox(width=6, from_=0, to=5)    # Кнопка Avarage CPI
spin1.place(x=310, y=303)

spin2 = Spinbox(width=6, from_=0, to=5)    # Кнопка Th Semester
spin2.place(x=420, y=303)

spin3 = Spinbox(width=8, from_=0, to=10)    # Кнопка Experience
spin3.place(x=310, y=353)

root.mainloop()
