from tkinter import *
import time
import string
import random


class Menu_game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("300x300")
        self.iconbitmap("Pythonsignev.ico")
        self.title("Game for Bdouilleurs")
        self.config(background='#3FAC17')
        self.resizable(width=False, height=False)

        self.create_text_button()

    def create_text_button(self):
        self.text  = Label(self, text='Welcome, \n wich level would you play ?', bg='#3FAC17', font=('Impossible', 20))

        self.button_level1 = Button(self, text='Level 1', bg='#3FAC17', font=('Impossible', 20), width=6, command=self.level_one)

        self.button_level2 = Button(self, text='Level 2', bg='#3FAC17', font=('Impossible', 20), width=6)

        self.text.pack()
        self.button_level1.pack()
        self.button_level2.pack(pady=10)

    def level_one(self):
        level = Level_one()
        self.quit()
        level.mainloop()


class Level_one(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("500x500")
        self.iconbitmap("Pythonsignev.ico")
        self.title("Level 1")
        self.config(background='#3FAC17')
        self.resizable(width=False, height=False)

        self.letter = 0
        self.morse = string.morse_case
        self.can = Canvas(self, width=500, height=450, bg='#3FAC17', bd=0)

        self.entry = Entry(self, font=('Impossible', 30), width=20, bg='#3FAC30')

        self.can.pack()
        self.play()


    def play(self):
        self.letter = random.randint(0, 26)
        self.text = self.can.create_text(250, 50, text=self.morse[self.letter], font=('Impossible', 30), fill='white')
        self.entry.pack(side=BOTTOM)
        print(self.letter)
        print(string.ascii_lowercase[self.letter])
        for i in range(45):
            self.can.move(self.text, 0, 10)
            time.sleep(0.5)
            self.can.update()
            if self.entry.get() == string.ascii_lowercase[self.letter] or self.entry.get() == string.ascii_uppercase[self.letter]:
                self.can.destroy(self.text)
                self.play()
            else:
                pass



menu = Menu_game()
menu.mainloop()
