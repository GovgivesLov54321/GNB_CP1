# GNB - 1st - 🔨 Turtle Race
import random as r
import turtle as t

turtle1 = t.Turtle()
turtle2 = t.Turtle()
turtle3 = t.Turtle()
turtle4 = t.Turtle()
turtle5 = t.Turtle()
line = t.Turtle()

turtle1.shape("turtle")
turtle2.shape("turtle")
turtle3.shape("turtle")
turtle4.shape("turtle")
turtle5.shape("turtle")
line.shape("arrow")

turtle1.color("black")
turtle2.color("pink")
turtle3.color("green")
turtle4.color("blue")
turtle5.color("orange")
line.color("black")

def setup():
    turtle1.teleport(-500, 400)
    turtle2.teleport(-500, 300)
    turtle3.teleport(-500, 200)
    turtle4.teleport(-500, 100)
    turtle5.teleport(-500, 0)
    line.teleport(500, -100)

    line.left(90)
    line.forward(600)

    line.hideturtle()

setup()

def race():
    while True:
        turtle1.forward(r.randint(1, 15))
        turtle2.forward(r.randint(1, 15))
        turtle3.forward(r.randint(1, 15))
        turtle4.forward(r.randint(1, 15))
        turtle5.forward(r.randint(1, 15))

race()

def winner():
    if turtle1.goto(500,0):
        t.done()
    elif turtle2.goto(500,0):
        t.done()
    elif turtle3.goto(500,0):
        t.done()
    elif turtle4.goto(500,0):
        t.done()
    else:
        t.done()
winner()



