# GNB - 1st - 🔨 Maze Generator
import random as r
import turtle as t

# Set up the screen size to fit the entire maze
screen = t.Screen()
screen.setup(width=1000, height=1000)
screen.setworldcoordinates(-450, -450, 450, 450)

# Create turtles
maze_drawer1 = t.Turtle()
maze_drawer1.shape("circle")

maze_drawer2 = t.Turtle()
maze_drawer2.shape("circle")

maze_drawer3 = t.Turtle()
maze_drawer3.shape("turtle")

# Grid setup (6x6)
rows = 6
cols = 6
grid = [[r.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Create a guaranteed path from entrance to exit
# Path goes down the left edge, then across the bottom
for i in range(rows):
    grid[i][0] = 0  # Clear left column
for j in range(cols):
    grid[-1][j] = 0  # Clear bottom row

print(grid)  # show grid layout 

# Setup function (border with openings)
def set_up():
    # Left border drawer
    maze_drawer1.penup()
    maze_drawer1.goto(-400, 400)
    maze_drawer1.pendown()
    maze_drawer1.right(90)
    maze_drawer1.forward(400)  # left border
    maze_drawer1.left(90)
    maze_drawer1.forward(370)  # shortened to leave gap at bottom-right

    maze_drawer2.penup()
    maze_drawer2.goto(0, 0)
    maze_drawer2.pendown()
    maze_drawer2.left(90)
    maze_drawer2.forward(400)  # right border

    # Top border (leave opening)
    maze_drawer2.left(90)
    maze_drawer2.forward(370)  # shortened to leave gap at top-left

    maze_drawer1.hideturtle()
    maze_drawer2.hideturtle()

set_up()

# Draw walls inside the maze
def draw_walls():
    cell_size = 60
    maze_drawer3.penup()
    maze_drawer3.speed(0)
    start_x, start_y = -400, 400

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * cell_size
            y = start_y - row * cell_size
            maze_drawer3.goto(x, y)
            if grid[row][col] == 1:
                maze_drawer3.pendown()
                maze_drawer3.fillcolor("black")
                maze_drawer3.begin_fill()
                for _ in range(4):
                    maze_drawer3.forward(cell_size)
                    maze_drawer3.right(90)
                maze_drawer3.end_fill()
                maze_drawer3.penup()
    
    maze_drawer3.hideturtle()

draw_walls()

# Print message about solvability
def is_solvable():
    print("Maze drawn with open entrance (top-left) and open exit (bottom-right).")

is_solvable()

t.done()