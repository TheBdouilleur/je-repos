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
score = 0
width = 500
height = 400
# TODO:add icon support
# TODO: IS DEAD AND TO DIE METHODS
# TODO: dynamize item position so that they react correctly to window resize
def start():
    text1 = Text(win, height=height, width=width)
    text1.config(state='normal', font=('Impossible', 30))
    text1.pack()
    '''for char in "MISSION:IMPOSSIBLE Your mission, should you choose to accept it, is to resist to the pikes This message will self destroy in 5 seconds":
        char = StringVar(value=char)
        startVariable.set(startVariable["value"]+char["value"])
        time.sleep(0.2)
        startLabel.pack()
        win.update()'''


def displayScore():
    global textbox1
    canvas.delete(textbox1)
    textbox1 = canvas.create_text(400, 30, text='SCORE: ' + str(score), fill='red',  font=('Impossible', 30))


def displayTime():
    time = round(getTime(), 2)
    print(time)
    global textbox2
    canvas.delete(textbox2)
    textbox2 = canvas.create_text(70, 30, text='TIME: ' + str(time), fill='red',  font=('Impossible', 30))


def getTime():
    actual_time = time.time()
    elapsed_time = actual_time - startTime
    return elapsed_time


def toDie():
    is_dead = guy.is_dead()
    if is_dead == 1:
        canvas.delete(pikeid)
        canvas.delete('all')
        print('Guy is dead...')
    else:
        pass
    return is_dead

class Guy:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.ballid = canvas.create_rectangle(10, 10, 100, 100, fill=color)
        self.canvas.move(self.ballid, width/2, height-100)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.x = 0

    def get_coords(self):
        guyCoords = self.canvas.coords(self.ballid)
        print(guyCoords)
        return guyCoords

    def is_dead(self):
        gc = guy.get_coords()
        pc = pike.get_coords()
        if pc[3] >= gc[1] and pc[2] >= gc[0] and pc[0] <= gc[2]:
            is_dead = 1
        else:
            is_dead = 0
        return is_dead

    def draw(self):
        self.canvas.move(self.ballid, self.x, 0)

    def turn_left(self, evtu):
        self.x = -2

    def turn_right(self, evtu):
        self.x = 2


class Pikes:
    def __init__(self, canvas, color):
        self.canvas = canvas
        ballcoords = guy.get_coords()
        ballcoords = ballcoords[0]
        self.x = random.randint(ballcoords-10, ballcoords+10)
        self.x2 = self.x + 30
        global pikeid
        self.pikeid = canvas.create_rectangle(self.x, -100, self.x2, 100, fill=color)
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
win.resizable(0, 0)
win.wm_attributes("-topmost", 1)
canvas = Canvas(win, width=width, height=height, bd=0, highlightthickness=0)
startVariable = StringVar()

# TODO: add background bg = PhotoImage(file="hangar.png")
startLabel = Label(win, textvariable=startVariable)
canvas.pack()
win.update()
# start()
guy = Guy(canvas, 'blue')
pike = Pikes(canvas, 'red')
canvas.pack()
win.update()
pikeid = None
ballid = None
textbox1 = None
textbox2 = None
startTime = time.time()

while 1:
    try:
        stop = toDie()
        if stop == 1:
            canvas.destroy()
            break
        guy.get_coords()
        pike.create_pike()
        pike.draw()
        guy.draw()
        win.update_idletasks()
        win.update()
        displayScore()
        displayTime()
        time.sleep(0.01)
    except TclError:
        print("App destroyed. Bye!")
        # time.sleep(2)
        sys.exit()

canvas = Canvas(win, width=width, height=height, bd=0, highlightthickness=0)
time = round(getTime(), 2)
canvas.create_text(60, 30, text='GAME OVER', fill='red',  font=('Impossible', 30))
canvas.create_text(80, 70, text='Final score: ' + str(score), fill='blue', font=('Impossible', 30))
canvas.create_text(120, 110, text='Elapsed time: ' + str(time), fill='green', font=('Impossible', 30))
canvas.pack()
win.update()

