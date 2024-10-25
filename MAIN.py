from turtle import *
import math

pensize(10)
hideturtle()

s = 1

def m(x):
    if x >= 0:
        return x
    elif x < 0:
        return x*-1

def f(x):
    y = x**2
    return y

posX = list()
posY = list()

def fillx(amount, type):
    global posX

    if type == "double":
        for i in range(amount*2):
            posX.append(-amount+i)
    else:
        for i in range(amount):
            posX.append(i)

def filly():
    global posX
    global posY

    for i in range(len(posX)):
        posY.append(f(posX[i]))

fillx(45, "double")
filly()

penup()
goto(posX[0]*s, posY[0]*s)
pendown()

for i in range(len(posX)):
    goto(posX[i]*s, posY[i]*s)

exitonclick()
