import turtle

def draw_heart():
    # Set up the turtle
    turtle.bgcolor("black")

    # List of colors to use for the heart
    colors = [
        "red", "orange", "yellow", "green", "cyan", "blue", 
        "indigo", "violet", "magenta", "pink", "purple", 
        "lightblue", "lightgreen", "gold", "brown", "salmon", 
        "crimson", "lime", "coral", "navy", "teal"
    ]
    
    # Start filling the heart shape with colors
    for i in range(len(colors)):
        turtle.color(colors[i])
        turtle.begin_fill()
        
        # Move the turtle to start position
        turtle.left(140)
        turtle.forward(112)  # Reduced size

        # Create the right curve
        turtle.circle(-56, 200)  # Reduced size

        # Create the left curve
        turtle.left(120)
        turtle.circle(-56, 200)  # Reduced size

        # Complete the shape
        turtle.forward(112)  # Reduced size
        turtle.end_fill()
        
        # Reset turtle position for the next color
        turtle.left(180)  # Turn around to start the next color
        turtle.forward(112)  # Move back to the starting point
        turtle.right(180)  # Face the original direction

    # Hide the turtle
    turtle.hideturtle()

# Set the turtle speed
turtle.speed(2)

# Call the draw_heart function
draw_heart()

# Finish the drawing
turtle.done()
