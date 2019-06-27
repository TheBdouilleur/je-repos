from tkinter import *

# Create the window
calculator = Tk()

# And personalize it
calculator.geometry("415x320")
calculator.title('Pocket calculator for Bdouilleurs')
calculator.iconbitmap('Pocket calculator.ico')
calculator.config(background='green')

can_button = Canvas(calculator, width=500, height=200, bg='black', bd=0, highlightthickness=0)
can_button.pack(side=BOTTOM, fill=X)

can_entry = Canvas(calculator, width=500, height=50, bg='black', bd=0, highlightthickness=0)
writing = Entry(can_entry, font=('Impossible', 30), bg='black', fg='green')
writing.pack(expand=YES, fill=X)
can_entry.pack(side=TOP, fill=X)
writing.delete(0, END)
global number
number = StringVar()
global plus
plus = False
global moins
moins = False

def Button_one():
    writing.insert(END, '1')


def Button_two():
    writing.insert(END, '2')


def Button_tree():
    writing.insert(END, '3')


def Button_four():
    writing.insert(END, '4')


def Button_five():
    writing.insert(END, '5')


def Button_six():
    writing.insert(END, '6')


def Button_seven():
    writing.insert(END, '7')


def Button_eight():
    writing.insert(END, '8')


def Button_nine():
    writing.insert(END, '9')


def plus_button():
    number = writing.get()
    number = int(number)
    print(number)
    writing.delete(0, END)
    plus = True


def moins_button():
    number = writing.get()
    number = int(number)
    print((number))
    writing.delete(0, END)
    moins = True


def equal_button():
    number2 = writing.get()
    number2 = int(number2, 16)
    print(number2)
    result = 0
    if plus:
        result = number + number2
    elif moins:
        result = number - number2
    result = str(result)
    print(result)
    writing.delete(0, END)
    writing.insert(0, result)


def clear_button():
    writing.delete(0, END)


button_one = Button(can_button, text=' 1 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                    command=Button_one)
button_two = Button(can_button, text=' 2 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                    command=Button_two)
button_tree = Button(can_button, text=' 3 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=Button_tree)
button_four = Button(can_button, text=' 4 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=Button_four)
button_five = Button(can_button, text=' 5 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=Button_five)
button_six = Button(can_button, text=' 6 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                    command=Button_six)
button_seven = Button(can_button, text=' 7 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=Button_seven)
button_eight = Button(can_button, text=' 8 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=Button_eight)
button_nine = Button(can_button, text=' 9 ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=Button_nine)
button_plus = Button(can_button, text=' + ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     textvariable=number, command=plus_button)
button_moins = Button(can_button, text=' - ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=moins_button)
button_multiply = Button(can_button, text='  X  ', font=('Impossible', 30), bg='green', fg='black', padx=15)
button_divise = Button(can_button, text=' / ', font=('Impossible', 30), bg='green', fg='black', padx=15)
button_equal = Button(can_button, text=' = ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=equal_button)
button_clear = Button(can_button, text=' C ', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=clear_button)


button_one.grid(row=0)
button_two.grid(row=0, column=1)
button_tree.grid(row=0, column=2)
button_four.grid(row=1)
button_five.grid(row=1, column=1)
button_six.grid(row=1, column=2)
button_seven.grid(row=2)
button_eight.grid(row=2, column=1)
button_nine.grid(row=2, column=2)
button_plus.grid(row=0, column=3)
button_moins.grid(row=0, column=4)
button_multiply.grid(row=1, column=3)
button_divise.grid(row=1,column=4)
button_equal.grid(row=2, column=3)
button_clear.grid(row=2, column=4)

calculator.mainloop()
