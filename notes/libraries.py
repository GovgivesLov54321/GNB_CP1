# GNB - 1st - ☑️Libraries and Built-In Functions
import random
import turtle as t

colors = ["orange", "green", "yellow", "red", "pink", "purple", "blue"]
side = random.randint(10,500)
t.color(random.choice(colors))
t.shape("")

t.fillcolor(random.choice(colors))
t.begin_fill()
for x in range(1,4):
    t.forward(side)
    t.right(90)
t.end_fill()


t.color("purple")

t.fillcolor("black")
t.begin_fill()

t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)

t.end_fill()

t.penup()
t.goto(50, 50)


t.color("dark blue")

t.fillcolor("light blue")
t.begin_fill()

t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)

t.end_fill()

t.done()

#or x in range(1,10):
 #   print(random.random())

