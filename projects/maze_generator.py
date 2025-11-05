# GNB - 1st - 🔨 Maze Generator
import random as r
import turtle as t

maze_drawer1 = t.Turtle()
maze_drawer1.shape("circle")

maze_drawer2 = t.Turtle()
maze_drawer2.shape("circle")

grid_rows = []
rows = []
grid_col = []
col = []

for row in rows:
    []


def set_up():
    maze_drawer1.teleport(-400, 400)
    maze_drawer2.teleport(0, 0)
    maze_drawer1.right(90)   
    maze_drawer2.left(90)
    maze_drawer1.forward(400)   
    maze_drawer2.forward(400)
    maze_drawer1.left(90)   
    maze_drawer2.left(90)
    maze_drawer1.forward(370)   
    maze_drawer2.forward(370)
    maze_drawer1.hideturtle()   
    maze_drawer2.hideturtle()
 
set_up()

def walls():
    help

walls()

def is_solvable():
    help

is_solvable()

t.done()