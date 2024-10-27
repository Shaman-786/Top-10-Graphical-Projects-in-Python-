import turtle
import random

def draw_flower():
    # Set up the turtle
    turtle.bgcolor("black")  # Background color
    turtle.speed(10)  # Set the speed of drawing
    turtle.pensize(2)  # Set the pen size

    # Extended list of colors for the petals
    colors = [
        "red", "orange", "yellow", "green", "blue",
        "indigo", "violet", "pink", "purple", "cyan",
        "magenta", "gold", "lightblue", "lime", "coral",
        "salmon", "tan", "navy", "teal", "brown", 
        "peach", "lavender", "chartreuse", "crimson", 
        "plum", "goldenrod", "skyblue", "forestgreen", 
        "darkorange", "lightgreen", "orchid"
    ]

    # Function to draw a petal
    def draw_petal():
        # Choose a random color for each petal
        turtle.color(random.choice(colors))
        turtle.circle(100, 60)  # Draw a curve
        turtle.left(120)  # Turn left to draw the other side
        turtle.circle(100, 60)  # Draw the second curve
        turtle.left(120)  # Reset direction for the next petal

    # Draw multiple petals
    for _ in range(12):  # Draw 12 petals
        draw_petal()
        turtle.right(30)  # Turn right to position for the next petal

    # Draw the center of the flower
    turtle.penup()
    turtle.goto(0, -20)  # Move to position for center
    turtle.pendown()
    turtle.color("yellow")  # Center color
    turtle.begin_fill()
    turtle.circle(20)  # Draw the center circle
    turtle.end_fill()

# Run the drawing function
draw_flower()

# Finish the drawing
turtle.hideturtle()  # Hide the turtle cursor
turtle.done()
