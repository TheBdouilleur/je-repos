#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Created on Fri Jun  7 17:45:28 2019



@author: the_bdouilleur

"""

# arcade game

from tkinter import *

import random

import time

import sys

global hitBottom

hitBottom = 0  # 0 because there is a pike and it hasn't hit the bottom yet

global pikeid

global ballid

global score

global textbox

score = 1

width = 500

height = 400


# TODO:add icon support

# TODO: IS DEAD AND TO DIE METHODS

# TODO: dynamize item position so that they react correctly to window resize


def display_score():
    global textbox1

    canvas.delete(textbox1)

    textbox1 = canvas.create_text(400, 30, text='SCORE: ' + str(score), fill='red', font=('Impossible', 30))


def display_time():
    time = round(getTime(), 1)

    print(time)

    global textbox2

    canvas.delete(textbox2)

    textbox2 = canvas.create_text(60, 30, text='TIME: ' + str(time), fill='red', font=('Impossible', 30))


def get_time():
    actual_time = time.time()

    elapsed_time = actual_time - startTime

    return elapsed_time


def to_die():
    is_dead = guy.is_dead()

    if is_dead == 1:

        canvas.delete(pikeid)

        canvas.delete(ballid)

    else:

        pass


class Guy:

    def __init__(self, canvas, color):
        self.canvas = canvas

        self.ballid = canvas.create_oval(10, 10, 100, 100, fill=color)

        self.canvas.move(self.ballid, width / 2, height - 100)

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        self.x = 0

    def get_coords(self):
        guyCoords = self.canvas.coords(self.ballid)

        print('guy coords:', guyCoords)

        return guyCoords

    def is_dead(self):
        bc = guy.get_coords()

        pc = pike.get_coords()

        '''if bc[]:

            is_dead = 1

        else:

            is_dead = 0

        return is_dead'''

    def draw(self):
        self.canvas.move(self.ballid, self.x, 0)
        guyCoords = self.canvas.coords(self.ballid)
        if guyCoords[1] < 0 or guyCoords[3] > 600:
            print('Guy is exit')

    def turn_left(self, evtu):
        self.x = -2

    def turn_right(self, evtu):
        self.x = 2


class Pikes:

    def __init__(self, canvas, color):

        self.canvas = canvas

        ballcoords = guy.get_coords()

        ballcoords = ballcoords[0]

        self.x = random.randint(ballcoords - 10, ballcoords + 10)

        self.x2 = self.x + 30

        global pikeid

        self.pikeid = canvas.create_rectangle(self.x, -900, self.x2, 100, fill=color)

        # print('pike class created')

        # print(canvas.coords(self.pikeid))

    def draw(self):

        global pikeid

        self.canvas.move(self.pikeid, 0, 3.15)

    def get_coords(self):

        pikecoords = self.canvas.coords(self.pikeid)

        return pikecoords

    def create_pike(self):

        global posball

        global pikeid

        posball = canvas.coords(self.pikeid)

        global hitBottom

        if hitBottom == 1:

            self.canvas.delete(self.pikeid)

            global pike

            pike = Pikes(canvas, 'red')

            global score

            score = score + 1

            hitBottom = 0

        else:

            pass

        if posball[3] >= height:
            hitBottom = 1


win = Tk()

win.title("Game")

win.resizable(1, 0)

win.wm_attributes("-topmost", 1)

canvas = Canvas(win, width=width, height=height, bd=0, highlightthickness=0)

# TODO: add background bg = PhotoImage(file="hangar.png")

guy = Guy(canvas, 'blue')

pike = Pikes(canvas, 'red')

canvas.pack()

win.update()

textbox1 = None

textbox2 = None

startTime = time.time()

while 1:

    try:

        guy.is_dead()

        guy.get_coords()

        pike.create_pike()

        pike.draw()

        guy.draw()

        win.update_idletasks()

        win.update()

        display_score()

        display_time()

        time.sleep(0.001)

    except TclError:

        print("App destroyed. Bye!")

        # time.sleep(2)

        sys.exit()
