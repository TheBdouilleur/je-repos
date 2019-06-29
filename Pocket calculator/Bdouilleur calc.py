from tkinter import *

# Create the window
calculator = Tk()

# And personalize it
width = 335
height = 405
geometrie = "{}x{}".format(width, height)
calculator.geometry(geometrie)
calculator.resizable(0, 0)
calculator.title('Pocket calculator for Bdouilleurs')
calculator.iconbitmap('Pythonsignev.ico')
calculator.config(background='green')

can_button = Canvas(calculator, width=500, height=200, bg='black', bd=0, highlightthickness=0)
can_button.pack(side=BOTTOM, fill=X)

can_entry = Canvas(calculator, width=500, height=50, bg='black', bd=0, highlightthickness=0)
writing = Entry(can_entry, font=('Impossible', 30), bg='black', fg='green')
writing.pack(expand=YES, fill=X)
can_entry.pack(side=TOP, fill=X)
writing.delete(0, END)

number = IntVar()

number2 = IntVar()

p = False
moins = False
mult = False
div = False


def zero_button(evt = None):
    writing.insert(END, '0')


def one_button(evt = None):
    writing.insert(END, '1')


def two_button(evt = None):
    writing.insert(END, '2')


def three_button(evt = None):
    writing.insert(END, '3')


def four_button(evt = None):
    writing.insert(END, '4')


def five_button(evt = None):
    writing.insert(END, '5')


def six_button(evt=None):
    writing.insert(END, '6')


def seven_button(evt = None):
    writing.insert(END, '7')


def eight_button(evt = None):
    writing.insert(END, '8')


def nine_button(evt = None):
    writing.insert(END, '9')


def point_button(evt = None):
    writing.insert(END, '.')


def plus_button(evt = None):
    global p
    global number
    number = writing.get()
    writing.delete(0, END)
    p = True


def moins_button(evt = None):
    global moins
    global number
    number = writing.get()
    writing.delete(0, END)
    moins = True


def multiply_button(evt = None):
    global mult
    global number
    number = writing.get()
    writing.delete(0, END)
    mult = True


def division_button(evt = None):
    global div
    global number
    number = writing.get()
    writing.delete(0, END)
    div = True


def equal_button(evt = None): # TODO: entry key for equal
    global p
    global moins
    global number
    global mult
    global div
    number2 = writing.get()
    number2 = float(number2)
    number = float(number)
    result = 0
    if p:
        result =number + number2
        p = False
    elif moins:
        result = number - number2
        moins = False
    elif mult:
        result = number * number2
        mult = False
    elif div:
        result = number / number2
        div = False

    writing.delete(0, END)
    writing.insert(0, result)


def clear_button(evt = None):
    writing.delete(0, END)


button_zero = Button(can_button, text='0', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=zero_button, width=2)
button_one = Button(can_button, text='1', font=('Impossible', 30), bg='green', fg='black', padx=15,
                    command=one_button, width=2)
button_two = Button(can_button, text='2', font=('Impossible', 30), bg='green', fg='black', padx=15,
                    command=two_button, width=2)
button_tree = Button(can_button, text='3', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=three_button, width=2)
button_four = Button(can_button, text='4', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=four_button, width=2)
button_five = Button(can_button, text='5', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=five_button, width=2)
button_six = Button(can_button, text='6', font=('Impossible', 30), bg='green', fg='black', padx=15,
                    command=six_button, width=2)
button_seven = Button(can_button, text='7', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=seven_button, width=2)
button_eight = Button(can_button, text='8', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=eight_button, width=2)
button_nine = Button(can_button, text='9', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=nine_button, width=2)
button_plus = Button(can_button, text='+', font=('Impossible', 30), bg='green', fg='black', padx=15,
                     command=plus_button, width=2)
button_moins = Button(can_button, text='-', font=('Impossible', 30), bg='green', fg='black', padx=15
                      , command=moins_button, width=2)
button_multiply = Button(can_button, text='X', font=('Impossible', 30), bg='green', fg='black', padx=15,
                         command=multiply_button, width=2)
button_divise = Button(can_button, text='/', font=('Impossible', 30), bg='green', fg='black', padx=15,
                       command=division_button, width=2)
button_equal = Button(can_button, text='=', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=equal_button, width=7)
button_clear = Button(can_button, text='C', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=clear_button, width=2)
button_point = Button(can_button, text='.', font=('Impossible', 30), bg='green', fg='black', padx=15,
                      command=point_button, width=2)

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
button_equal.grid(row=2, column=3, columnspan=2)
button_clear.grid(row=3, column=0)
button_zero.grid(row=3, column=1)
button_point.grid(row=3, column=2)


calculator.bind('1', one_button)
calculator.bind('2', two_button)
calculator.bind('3', three_button)
calculator.bind('4', four_button)
calculator.bind('5', five_button)
calculator.bind('6', six_button)
calculator.bind('7', seven_button)
calculator.bind('8', eight_button)
calculator.bind('9', nine_button)
calculator.bind('0', zero_button)
calculator.bind('c', clear_button)
calculator.bind('C', clear_button)
calculator.bind('.', point_button)
calculator.bind('+', plus_button)
calculator.bind('-', moins_button)
calculator.bind('*', multiply_button)
calculator.bind('/', division_button)
calculator.bind("<Return>", equal_button)


calculator.mainloop()
