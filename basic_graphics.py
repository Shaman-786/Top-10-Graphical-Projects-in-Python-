import turtle

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
t = turtle.Turtle()
t.speed(3)  # Moderate speed for drawing
t.pensize(2)  # Thickness of the drawing line
t.shape("turtle")

# Define colors for pattern
colors = ["red", "blue", "green", "purple"]

# Create a square pattern
for i in range(4):
    t.pencolor(colors[i])  # Change pen color
    t.forward(100)  # Move turtle forward by 100 units
    t.right(90)  # Turn turtle by 90 degrees

# Draw a circle at the center of the square
t.penup()  # Lift pen to move without drawing
t.goto(0, -50)  # Move to the circle's starting position
t.pendown()  # Place pen down to start drawing
t.pencolor("orange")
t.circle(50)  # Draw circle with radius 50

# End turtle graphics
turtle.done()
