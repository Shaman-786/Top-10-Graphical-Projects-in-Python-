import turtle
import colorsys

# Setup the turtle window
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.tracer(10)  # Optimize for faster drawing

hue = 0.0

# Loop to create the rotating design
for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
    t.pencolor(color)  # Set the color of the turtle pen
    t.width(2)
    t.forward(i * 1.5)  # Move turtle forward
    t.left(59)  # Rotate the turtle
    hue += 0.005  # Increment hue for different colors

turtle.done()
