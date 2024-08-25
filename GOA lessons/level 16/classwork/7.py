from turtle import *

speed(20)
width(7)

def square(size):
    for i in range(4):
        forward(size)
        left(90)

def move(x, y):
    penup()
    goto(x, y)
    pendown()

square(250)
move(-280, 0)
square(250)
move(-280, -280)
square(250)
move(0, -280)
square(250)



exitonclick()