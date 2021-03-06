"""
@autor = TheBdouilleur2
"""

from tkinter import *
import time
import string
import random


class Menu_game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("300x300")
        self.iconbitmap("C:/Users\hubert et Agnès\Documents\The Bdouilleur2 space\Missions in python/Pythonsignev.ico")
        self.title("Game for Bdouilleurs")
        self.config(background='#3FAC17')
        self.resizable(width=False, height=False)

        self.create_text_button()

    def create_text_button(self):
        self.text  = Label(self, text='Welcome, \n wich level would you play ?', bg='#3FAC17', font=('Impossible', 20))

        self.button_level1 = Button(self, text='Level 1', bg='#3FAC17', font=('Impossible', 20), width=6, command=self.level_one)

        self.button_level2 = Button(self, text='Level 2', bg='#3FAC17', font=('Impossible', 20), width=6, command=self.level_two)

        self.text.pack()
        self.button_level1.pack()
        self.button_level2.pack(pady=10)

    def level_one(self):
        level = Level(0.5)
        self.quit()
        level.mainloop()

    def level_two(self):
        level = Level(0.25)
        self.quit()
        level.mainloop()


class Level(Tk):
    def __init__(self, time):
        Tk.__init__(self)
        self.geometry("500x500")
        self.iconbitmap("C:/Users\hubert et Agnès\Documents\The Bdouilleur2 space\Missions in python/Pythonsignev.ico")
        self.title("Level 1")
        self.config(background='#3FAC17')
        self.resizable(width=False, height=False)

        self.letter = 0
        self.morse = string.morse_case
        self.can = Canvas(self, width=500, height=450, bg='#3FAC17', bd=0)
        self.heart_image = PhotoImage(file="heart.png", master=self.can)
        self.heart = self.can.create_image((20, 20), image=self.heart_image)
        self.time = time
        self.time_save = time
        self.live = 5

        self.frame = Frame(self, bg='#3FAC17')

        self.live_text = self.can.create_text(50, 20, text=self.live, font=('Impossible', 25))
        self.entry = Entry(self.frame, font=('Impossible', 30), width=20, bg='#3FAC30')

        self.pass_button = Button(self.frame, font=('Impossible', 25), text='PASS', bg='#9FAC17', command=self.pass_b)

        self.can.pack()
        self.entry.pack(side=LEFT, padx=15)
        self.pass_button.pack(side=RIGHT)
        self.frame.pack(side=BOTTOM)
        self.play()

    def play(self):
        self.letter = random.randint(0, 25)
        self.text = self.can.create_text(250, 50, text=self.morse[self.letter], font=('Impossible', 30), fill='white')
        for i in range(45):
            self.can.move(self.text, 0, 10)
            time.sleep(self.time)
            self.can.update()
            if self.entry.get() == string.ascii_lowercase[self.letter] or self.entry.get() == string.ascii_uppercase[self.letter]:
                self.can.delete(self.text)
                self.entry.delete(0, END)
                self.play()
            if self.can.coords(self.text)[1] > 440:
                self.can.delete(self.text)
                self.entry.delete(0, END)
                self.entry.insert(0, string.ascii_uppercase[self.letter])
                if self.live == 0:
                    self.can.create_text(250, 200, text='Game Over', font=('Impossible', 30))
                    self.can.update()
                    time.sleep(3)
                    quit()
                self.live -=1
                self.can.delete(self.live_text)
                self.live_text = self.can.create_text(50, 20, text=self.live, font=('Impossible', 25))
                self.time = self.time_save

    def pass_b(self):
        self.time = 0.01



if __name__ == '__main__':
    try:
        menu = Menu_game()
        menu.mainloop()
    except TclError:
        print('App was destroy')
        quit()
