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
    turtle1.teleport(-200, 400)
    turtle2.teleport(-200, 300)
    turtle3.teleport(-200, 200)
    turtle4.teleport(-200, 100)
    turtle5.teleport(-200, 0)
    line.teleport(500, -100)

    line.left(90)
    line.forward(600)

    line.hideturtle()

setup()

def race():
    for t in t:
        turtle1.forward(r.randint(1, 30))

race()
t.done()





















