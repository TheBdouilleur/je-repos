from tkinter import *


class Calculate(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.width = 431
        self.height = 430
        self.number = IntVar()
        self.number2 = IntVar()
        self.p = False
        self.moins = False
        self.mult = False
        self.div = False
        self.sqrt = False
        self.square = False
        self.result = 0
        
        #Color
        self.button_number_color = '#179A04'
        self.button_op_color = 'green'

        self.geometrie = "{}x{}".format(self.width, self.height)
        self.geometry(self.geometrie)
        self.resizable(0, 0)
        self.title('Pocket calculator for Bdouilleurs')
        #self.iconbitmap('Pythonsignev.ico')
        self.config(background='green')
        self.can_button = Canvas(self, width=500, height=50, bg='black', bd=0, highlightthickness=0)
        self.can_button.pack(side=BOTTOM, fill=X)
        self.can_entry = Canvas(self, width=500, height=50, bg='black', bd=0, highlightthickness=0)
        self.writing = Entry(self.can_entry, font=('Impossible', 30), bg='black', fg='green')
        self.writing.pack(expand=YES, fill=X)
        self.can_entry.pack(side=TOP, fill=X)
        self.writing.delete(0, END)

        self.create_button()
        self.grid_button()
        self.bind_calculator()

        self.create_menu()
        self.config(menu=self.menu)

    def create_button(self):
        self.button_zero = Button(self.can_button, text='0', font=('Impossible', 30), bg=self.button_number_color, fg='black', padx=15,
                                  command=self.zero_button, width=2)
        self.button_one = Button(self.can_button, text='1', font=('Impossible', 30), bg=self.button_number_color, fg='black', padx=15,
                                 command=self.one_button, width=2)
        self.button_two = Button(self.can_button, text='2', font=('Impossible', 30), bg=self.button_number_color, fg='black', padx=15,
                                 command=self.two_button, width=2)
        self.button_tree = Button(self.can_button, text='3', font=('Impossible', 30), bg=self.button_number_color, fg='black', padx=15,
                                  command=self.three_button, width=2)
        self.button_four = Button(self.can_button, text='4', font=('Impossible', 30), bg=self.button_number_color, fg='black', padx=15,
                                  command=self.four_button, width=2)
        self.button_five = Button(self.can_button, text='5', font=('Impossible', 30), bg=self.button_number_color, fg='black', padx=15,
                                  command=self.five_button, width=2)
        self.button_six = Button(self.can_button, text='6', font=('Impossible', 30), bg=self.button_number_color, fg='black', padx=15,
                                 command=self.six_button, width=2)
        self.button_seven = Button(self.can_button, text='7', font=('Impossible', 30), bg=self.button_number_color, fg='black',
                                   padx=15,
                                   command=self.seven_button, width=2)
        self.button_eight = Button(self.can_button, text='8', font=('Impossible', 30), bg=self.button_number_color, fg='black',
                                   padx=15,
                                   command=self.eight_button, width=2)
        self.button_nine = Button(self.can_button, text='9', font=('Impossible', 30), bg=self.button_number_color, fg='black', padx=15,
                                  command=self.nine_button, width=2)
        self.button_plus = Button(self.can_button, text='+', font=('Impossible', 30), bg=self.button_op_color, fg='black', padx=15,
                                  command=self.plus_button, width=2)
        self.button_moins = Button(self.can_button, text='-', font=('Impossible', 30), bg=self.button_op_color, fg='black',
                                   command=self.moins_button
                                   , padx=15, width=2)
        self.button_multiply = Button(self.can_button, text='X', font=('Impossible', 30), bg=self.button_op_color, fg='black',
                                      padx=15,
                                      command=self.multiply_button, width=2)
        self.button_divise = Button(self.can_button, text='÷', font=('Impossible', 30), bg=self.button_op_color, fg='black', padx=15,
                                    command=self.division_button, width=2)
        self.button_equal = Button(self.can_button, text='=', font=('Impossible', 30), bg=self.button_op_color, fg='black', padx=15,
                                   command=self.equal_button, width=5)
        self.button_clear = Button(self.can_button, text='C', font=('Impossible', 30), bg=self.button_op_color, fg='black', padx=15,
                                   command=self.clear_button, width=2)
        self.button_point = Button(self.can_button, text='.', font=('Impossible', 30), bg=self.button_op_color, fg='black', padx=15,
                                   command=self.point_button, width=2)
        self.button_sqrt = Button(self.can_button, text='√', font=('Impossible', 30), bg=self.button_op_color, fg='black', padx=15,
                                  command=self.sqrt_button, width=2)
        self.button_square = Button(self.can_button, text='^2', font=('Impossible', 30), bg=self.button_op_color, fg='black',
                                    padx=15,
                                    command=self.square_button, width=2)

        self.button_pm = Button(self.can_button, text='±', font=('Impossible', 30), bg=self.button_op_color, fg='black',
                                    padx=15, width=2, command=self.pm_button)
        # self.button_infinite = Button(self.can_button, text="¯", font=('Impossible', 30), bg='green', fg='black',
        #                              padx=15, width=2, command=self.infinite_button)

    def grid_button(self):
        self.button_one.grid(row=1)
        self.button_two.grid(row=1, column=1)
        self.button_tree.grid(row=1, column=2)
        self.button_four.grid(row=2)
        self.button_five.grid(row=2, column=1)
        self.button_six.grid(row=2, column=2)
        self.button_seven.grid(row=3)
        self.button_eight.grid(row=3, column=1)
        self.button_nine.grid(row=3, column=2)
        self.button_plus.grid(row=2, column=3)
        self.button_moins.grid(row=2, column=4)
        self.button_multiply.grid(row=3, column=3)
        self.button_divise.grid(row=3, column=4)
        self.button_equal.grid(row=4, column=3, columnspan=2)
        self.button_clear.grid(row=0, column=0)
        self.button_zero.grid(row=4, column=1)
        self.button_point.grid(row=4, column=2)
        self.button_sqrt.grid(row=1, column=3)
        self.button_square.grid(row=1, column=4)
        self.button_pm.grid(row=4)
        # self.button_infinite.grid(row=0, column=1)

    def bind_calculator(self):
        self.bind('1', self.one_button)
        self.bind('<KP_1>', self.one_button)
        self.bind('2', self.two_button)
        self.bind('<KP_2>', self.two_button)
        self.bind('3', self.three_button)
        self.bind('<KP_3>', self.three_button)
        self.bind('4', self.four_button)
        self.bind('<KP_4>', self.four_button)
        self.bind('5', self.five_button)
        self.bind('<KP_5>', self.five_button)
        self.bind('6', self.six_button)
        self.bind('<KP_6>', self.six_button)
        self.bind('7', self.seven_button)
        self.bind('<KP_7>', self.seven_button)
        self.bind('8', self.eight_button)
        self.bind('<KP_8>', self.eight_button)
        self.bind('9', self.nine_button)
        self.bind('<KP_9>', self.nine_button)
        self.bind('0', self.zero_button)
        self.bind('<KP_0>', self.zero_button)
        self.bind('c', self.clear_button)
        self.bind('C', self.clear_button)
        self.bind('<BackSpace>', self.clear_button)
        self.bind('.', self.point_button)
        self.bind('+', self.plus_button)
        self.bind('<KP_Add>', self.plus_button)
        self.bind('-', self.moins_button)
        self.bind('<KP_Subtract>', self.moins_button)
        self.bind('*', self.multiply_button)
        self.bind('/', self.division_button)
        self.bind("<Return>", self.equal_button)
        self.bind("<KP_Enter>", self.equal_button)

    def create_menu(self):
        self.menu = Menu(self)
        self.menu_file = Menu(self.menu, tearoff=0)
        self.menu_file.add_command(label="New", command=self.new_menu)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Quit', command=self.quit)
        self.menu.add_cascade(label='File', menu=self.menu_file)

        self.menu_help = Menu(self.menu, tearoff=0)
        self.menu_help.add_command(label='About us', command=self.menu_aboutus)
        self.menu.add_cascade(label='Help', menu=self.menu_help)

    def zero_button(self, evt=None):
        self.writing.insert(END, '0')

    def one_button(self, evt=None):
        self.writing.insert(END, '1')

    def two_button(self, evt=None):
        self.writing.insert(END, '2')

    def three_button(self, evt=None):
        self.writing.insert(END, '3')

    def four_button(self, evt=None):
        self.writing.insert(END, '4')

    def five_button(self, evt=None):
        self.writing.insert(END, '5')

    def six_button(self, evt=None):
        self.writing.insert(END, '6')

    def seven_button(self, evt=None):
        self.writing.insert(END, '7')

    def eight_button(self, evt=None):
        self.writing.insert(END, '8')

    def nine_button(self, evt=None):
        self.writing.insert(END, '9')

    def point_button(self, evt=None):
        self.writing.insert(END, '.')

    def plus_button(self, evt=None):
        self.number = self.writing.get()
        self.writing.delete(0, END)
        self.p = True

    def moins_button(self, evt=None):
        self.number = self.writing.get()
        self.writing.delete(0, END)
        self.moins = True

    def multiply_button(self, evt=None):
        self.number = self.writing.get()
        self.writing.delete(0, END)
        self.mult = True

    def division_button(self, evt=None):
        self.number = self.writing.get()
        self.writing.delete(0, END)
        self.div = True

    def sqrt_button(self, evt=None):
        self.number = self.writing.get()
        self.writing.delete(0, END)
        self.number = int(self.number)
        self.result = self.number ** 0.5
        self.writing.insert(0, self.result)

    def square_button(self, evt=None):
        self.number = self.writing.get()
        self.writing.delete(0, END)
        self.number = int(self.number)
        self.result = int(self.number ** 2)
        self.writing.insert(0, self.result)

    def equal_button(self, evt=None):
        self.number2 = self.writing.get()
        self.number2 = float(self.number2)
        self.number = float(self.number)
        self.result = 0
        if self.p:
            self.result = self.number + self.number2
            self.p = False
        elif self.moins:
            self.result = self.number - self.number2
            self.moins = False
        elif self.mult:
            self.result = self.number * self.number2
            self.mult = False
        elif self.div:
            self.result = self.number / self.number2
            self.div = False

        self.writing.delete(0, END)
        self.writing.insert(0, self.result)

    def clear_button(self, evt=None):
        self.writing.delete(0, END)

    def pm_button(self, evt=None):
        self.number = self.writing.get()
        self.number = float(self.number)
        self.number = -self.number
        self.writing.delete(0, END)
        self.writing.insert(0, self.number)

    # def infinite_button(self, evt=None):
     #   pass

    def new_menu(self):
        calculator2 = Calculate()

    def menu_aboutus(self):
        win = Tk()
        win.title('About us')
        win.iconbitmap('Pythonsignev.ico')
        win.geometry("300x200+200+50")
        message = Message(win, text='We are two JE (juneval expert), and we are two Bdouilleurs', font=('Impossible', 20))
        message.pack()
        win.mainloop()

# Create the window
calculator = Calculate()

calculator.mainloop()
