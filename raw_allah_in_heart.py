import turtle
import random
import time

def draw_allah_name():
    # Set up the turtle
    turtle.bgcolor("black")  # Background color
    turtle.speed(3)  # Set the speed of drawing

    # List of colors for the name
    colors = [
        "red", "orange", "yellow", "green", "blue", 
        "indigo", "violet", "pink", "purple", "cyan", 
        "magenta", "gold", "silver", "lime", "teal", 
        "coral", "navy", "brown", "crimson", "khaki"
    ]
    
    # Move the turtle to start position
    turtle.penup()
    turtle.goto(0, 0)  # Center position for the text
    turtle.pendown()

    # Draw "اللہ" with different colors
    turtle.pensize(5)  # Set the pen size

    for letter in "اللہ":
        # Randomly select a color for each letter
        color = random.choice(colors)
        turtle.color(color)

        # Draw each letter with a slight rotation for style
        turtle.write(letter, font=("Arial", 50, "bold"), align="center")
        turtle.right(10)  # Rotate slightly for the next letter
        turtle.penup()
        turtle.forward(60)  # Move forward to draw the next letter
        turtle.pendown()

    # Hide the turtle after drawing
    turtle.hideturtle()

    # Wait a moment before showing the complete written form
    time.sleep(1)

    # Move to display the complete name in written format
    turtle.penup()
    turtle.goto(0, -100)  # Move below the letters to display the message
    turtle.pendown()
    turtle.color("white")  # Set message color
    turtle.write("اللہ", font=("Arial", 50, "bold"), align="center")

    # Display completion message
    turtle.penup()
    turtle.goto(0, -160)  # Move further down to display the completion message
    turtle.pendown()
    turtle.write("Drawing Complete!", align="center", font=("Arial", 24, "bold"))

# Run the drawing function
draw_allah_name()

# Finish the drawing
turtle.done()
