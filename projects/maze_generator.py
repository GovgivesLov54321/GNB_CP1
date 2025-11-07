# GNB - 1st - 🔨 Maze Generator
import random as r
import turtle as t

maze_drawer1 = t.Turtle()
maze_drawer1.shape("circle")

maze_drawer2 = t.Turtle()
maze_drawer2.shape("circle")

maze_drawer3 = t.Turtle()
maze_drawer3.shape("turtle")

grid_rows = [[], [], [], [], [], []]
grid_cols = [[], [], [], [], [], []]


for iter,row in enumerate(grid_rows):
    if r.randint(0, 1)==1:
        row.append(1)
    else:
        row.append(0)

for iter,col in enumerate(grid_cols):
    if r.randint(0, 1)==1:
       col.append(1)
    else:
        col.append(0)



print(grid_rows)
print(grid_cols)



if row in grid_rows == 1:
    maze_drawer3.teleport(0, 0)
    t.pendown()
    maze_drawer3.forward(400)

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

def draw_walls():
   help

draw_walls()

def is_solvable():
    help

is_solvable()

t.done()