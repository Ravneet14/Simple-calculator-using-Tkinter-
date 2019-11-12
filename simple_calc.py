from tkinter import *

window = Tk()
window.configure(background = "blue")

window.title("Simple calculator")

entry1 = Entry(window)
entry1.grid(columnspan=4)


def myclick(number):
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current) + str(number))


def myclear():
    entry1.delete(0, END)


def myadd():
    global first_number
    first_number = entry1.get()
    entry1.delete(0, END)
    global count
    count = 1


def myequal():
    second_number = entry1.get()
    if count == 1:
        res = int(second_number) + int(first_number)
    elif count == 2:
        res = int(second_number) - int(first_number)
    elif count == 3:
        res = int(second_number) * int(first_number)
    elif count == 4:
        res = int(first_number) / int(second_number)
    entry1.delete(0, END)
    entry1.insert(0, res)


def mysub():
    global first_number
    first_number = entry1.get()
    entry1.delete(0, END)
    global count
    count = 2


def mymul():
    global first_number
    first_number = entry1.get()
    entry1.delete(0, END)
    global count
    count = 3


def mydiv():
    global first_number
    first_number = entry1.get()
    entry1.delete(0, END)
    global count
    count = 4


button1 = Button(window, text="1", fg="red", bg="yellow", command = lambda: myclick(1))
button2 = Button(window, text="2", fg="red", bg="yellow",command = lambda: myclick(2))
button3 = Button(window, text="3", fg="red", bg="yellow",command = lambda: myclick(3))
button4 = Button(window, text="4", fg="red", bg="yellow",command =lambda: myclick(4))
button5 = Button(window, text="5", fg="red", bg="yellow",command = lambda: myclick(5))
button6 = Button(window, text="6", fg="red", bg="yellow",command = lambda: myclick(6))
button7 = Button(window, text="7", fg="red", bg="yellow",command = lambda: myclick(7))
button8 = Button(window, text="8", fg="red", bg="yellow",command = lambda: myclick(8))
button9 = Button(window, text="9", fg="red", bg="yellow",command = lambda: myclick(9))
button10 = Button(window, text="0", fg="red", bg="yellow",command = lambda: myclick(0))
button11 = Button(window, text="Clear", fg="red", bg="yellow",command = myclear)
button12 = Button(window, text="=", fg="red", bg="yellow",command = myequal)
button13 = Button(window, text="+", fg="red", bg="yellow",command = myadd)
button14 = Button(window, text="-", fg="red", bg="yellow",command = mysub)
button15 = Button(window, text="*", fg="red", bg="yellow",command = mymul)
button16 = Button(window, text="/", fg="red", bg="yellow",command = mydiv)

button1.grid(row=1, column=0)
button4.grid(row=2, column=0)
button7.grid(row=3, column=0)
button10.grid(row=4, column=0)

button2.grid(row=1, column=1)
button5.grid(row=2, column=1)
button8.grid(row=3, column=1)
button11.grid(row=4, column=1)

button3.grid(row=1, column=2)
button6.grid(row=2, column=2)
button9.grid(row=3, column=2)
button12.grid(row=4, column=2)

button13.grid(row=1, column=3)
button14.grid(row=2, column=3)
button15.grid(row=3, column=3)
button16.grid(row=4, column=3)

button1.config(height = 10, width = 10)
button2.config(height = 10, width = 10)
button3.config(height = 10, width = 10)
button4.config(height = 10, width = 10)
button5.config(height = 10, width = 10)
button6.config(height = 10, width = 10)
button7.config(height = 10, width = 10)
button8.config(height = 10, width = 10)

button9.config(height = 10, width = 10)
button10.config(height = 10, width = 10)
button11.config(height = 10, width = 10)
button12.config(height = 10, width = 10)
button13.config(height = 10, width = 10)
button14.config(height = 10, width = 10)
button15.config(height = 10, width = 10)
button16.config(height = 10, width = 10)

window.mainloop()
