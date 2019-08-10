from tkinter import *
import time
import string


class Menu_game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("500x500")
        self.iconbitmap("Pythonsignev.ico")
        self.title("Game for Bdouilleurs")
        self.config(background='#3FAC17')
        self.resizable(width=False, height=False)

        self.create_text_button()

    def create_text_button(self):
        self.text  = Label(self, text = 'Welcome, \n wich level would you play ?', bg='#3FAC17', font=('Impossible', 20))

        self.button_level1 = Button(self, text='Level 1', bg='#3FAC17', font=('Impossible', 20))

        self.text.pack()
        self.button_level1.pack()

# can = tk.Canvas(win, width=500, height=500, bg='#3FAC17')
# text = can.create_text(50, 50, text='Hello', font=('Impossible', 30), fill='white')

#can.pack()

menu = Menu_game()
menu.mainloop()
