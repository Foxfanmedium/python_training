# coding utf-8

#import turtle
# import tkSimpleDialog  #2.x Python
#import random

#turtle.circle(20)
#turtle.speed(0) #accelerate moving of cursor

#answer = ''
#while answer != "N":
#    answer = turtle.textinput("Paint the circle", "Y/N")

#    if answer =="Y":
#        turtle.penup()  # make an transparent cursor
#        turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200)) # move the corsor to another place on display
#        turtle.pendown()   # make an transparent cursor
#        turtle.fillcolor(random.random(), random.random(),random.random) #fullfill inside space into circle by colour
#        turtle.begin_fill() #important before function of painting
#        turtle.circle(random.randrange(1, 100)) # random value fo radius
#        turtle.end_fill()   #important after function of painting
#    else:
#        pass
#=======================================================================================================================
# coding utf-8
# The Russian roulette

#import turtle
# import tkSimpleDialog  #2.x Python
#import random
#import math

#def gotoxy(x, y):
#    turtle.penup()
#    turtle.goto(x, y)
#    turtle.pendown()

#def draw_circle(r, color):
#    turtle.fillcolor(color)
#    turtle.begin_fill()
#    turtle.circle(r)
#    turtle.end_fill()

#turtle.speed(0) #accelerate moving of cursor

#gotoxy(0, 0)
#turtle.circle(80)
#gotoxy(0, 160)
#draw_circle(5, "red")

#phi = 360 / 7
#r = 50

# barrel for bullets
#for i in range(0, 7):
#    phi_rad = phi * i * math.pi / 180.0
#    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
#    turtle.circle(22)

# paint a bullet

#gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
#draw_circle(22, "brown")

#answer = ''
#while answer != "N":
#    answer = turtle.textinput("Paint the circle", "Y/N")

#    if answer =="Y":
#        turtle.penup()  # make an transparent cursor
#        turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200)) # move the corsor to another place on display
#        turtle.pendown()   # make an transparent cursor
#        turtle.fillcolor(random.random(), random.random(),random.random) #fullfill inside space into circle by colour
#        turtle.begin_fill() #important before function of painting
#        turtle.circle(random.randrange(1, 100)) # random value fo radius
#        turtle.end_fill()   #important after function of painting
#    else:
#        pass
#=======================================================================================================================
# Adding animation for Russian roulette

# coding utf-8
# The Russian roulette

import turtle
# import tkSimpleDialog  #2.x Python
import random
import math

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

gotoxy(0, 0)
turtle.circle(80)
gotoxy(0, 160)
draw_circle(5, "red")

phi = 360 / 7
r = 50

for i in range(0, 7):  # paint a barrel
    phi_rad = phi * i * math.pi / 180.0
    gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
    draw_circle(22, "white")

answer = ''
start = 0
while answer != "N":
    answer = turtle.textinput("Let's play!?", "Y/N")

    if answer == "Y":

        for i in range(start, random.randrange(7, 20)):  # random.randrange(7, 100)
            phi_rad = phi * i * math.pi / 180.0
            gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
            draw_circle(22, "brown")
            draw_circle(22, "white")


        gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
        draw_circle(22, "brown")

        start = i % 7
        if start == 0:
            gotoxy(-150, 250)
            turtle.write("You are failed!", font=("Arial", 18, "normal.py"))
#        turtle.penup()  # make an transparent cursor
#        turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200)) # move the corsor to another place on display
 #       turtle.pendown()   # make an transparent cursor
#        turtle.fillcolor(random.random(), random.random(),random.random) #fullfill inside space into circle by colour
#        turtle.begin_fill() #important before function of painting
 #       turtle.circle(random.randrange(1, 100)) # random value fo radius
 #       turtle.end_fill()   #important after function of painting
    else:
        pass


















































