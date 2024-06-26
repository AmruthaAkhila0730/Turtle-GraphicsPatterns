import turtle

# Function to draw a square pattern
def draw_square_pattern(artist):
    artist.penup()
    artist.goto(-250, 150)
    artist.pendown()
    artist.speed(0)
    artist.width(1)
    colors = ["red", "orange", "yellow", "green"]
    for x in range(90):
        artist.pencolor(colors[x % 4])
        artist.forward(x)
        artist.left(90)

# Function to draw a spiral pattern
def draw_spiral_pattern(artist):
    artist.penup()
    artist.goto(50, 150)
    artist.pendown()
    artist.speed(0)
    artist.width(2)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for x in range(90):
        artist.pencolor(colors[x % 6])
        artist.forward(x)
        artist.left(59)

# Function to draw a petal shape
def draw_petal(artist, size=100):
    artist.circle(size, 60)
    artist.left(120)
    artist.circle(size, 60)
    artist.left(120)

# Function to draw a flower pattern
def draw_flower(artist):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    artist.penup()
    artist.goto(-190, -110)
    artist.pendown()
    artist.speed(0)
    artist.width(1)
    petal_size = 120
    gap = 25 
    for _ in range(5):
        for __ in range(6):
            artist.pencolor(colors[__ % 6])
            draw_petal(artist, size=petal_size)
            artist.left(59)
        artist.penup()
        artist.pendown()
        

# Function to draw a circle pattern
def draw_circle_pattern(artist):
    artist.penup()
    artist.goto(80, -110)
    artist.pendown()
    artist.speed(0)
    artist.width(2)
    colors = ["red", "green", "blue", "yellow"]
    for x in range(90):
        artist.pencolor(colors[x % 4])
        artist.forward(x / 2)
        artist.left(25)

# Set up the screen
window = turtle.Screen()
window.bgcolor("white")

# Create four turtles named "artist1" to "artist4"
artist1 = turtle.Turtle()
artist2 = turtle.Turtle()
artist3 = turtle.Turtle()
artist4 = turtle.Turtle()

# Draw each pattern in its designated position
draw_square_pattern(artist1)
draw_spiral_pattern(artist2)
draw_flower(artist3)
draw_circle_pattern(artist4)

# Hide the turtles and display the window
artist1.hideturtle()
artist2.hideturtle()
artist3.hideturtle()
artist4.hideturtle()
window.mainloop()
