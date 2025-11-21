# GNB - 1st - Starter fr 21/11/25
import turtle as t

def draw_branch(length):
    if length > 5:
        for i in range(3):
            t.forward(length)
            draw_branch(length / 3)
            t.backward(length)
            t.right(60)

turtle = t.Turtle()
turtle.speed(15)
turtle.color("Light Blue")
turtle.penup
turtle.goto(-200, 0)
turtle.pendown

for i in range(6):
    draw_branch(100)
    turtle.right(60)