# GNB - 1st - 🔨 Maze Generator
import random as r
import turtle as t

maze_drawer1 = t.Turtle()
maze_drawer1.shape("circle")

maze_drawer2 = t.Turtle()
maze_drawer2.shape("circle")

grid_rows = [[], [], [], [], [], []]
grid_cols = [[], [], [], [], [], []]


for iter,row in enumerate(grid_rows):
    if r.randint(0, 1)==1:
        grid_rows[iter]=1

for iter,col in enumerate(grid_cols):
    if r.randint(0, 1)==1:
        grid_cols[iter]=1

print(grid_rows)
print(grid_cols)



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