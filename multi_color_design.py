# File Name: multi_color_design.py

import turtle

# Setup the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color to black

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the speed of the turtle to the maximum
pen.width(2)  # Set the pen width

# List of colors for the design
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Draw the design
for i in range(360):  # 360 iterations for a full circular design
    pen.pencolor(colors[i % 6])  # Cycle through the colors
    pen.forward(i * 3 / 4)  # Move the turtle forward
    pen.left(59)  # Turn the turtle left by 59 degrees

# Hide the turtle after the design is complete
pen.hideturtle()

# Keep the window open until closed by the user
turtle.done()
