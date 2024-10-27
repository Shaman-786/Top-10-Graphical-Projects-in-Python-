import turtle
import random

def draw_heart(x, y, color):
    # Move the turtle to the specified position
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    # Set up the turtle for the heart
    turtle.color(color)
    turtle.begin_fill()

    # Move the turtle to start position
    turtle.left(140)
    turtle.forward(112)  # Adjusted forward movement

    # Create the right curve
    turtle.circle(-56, 200)  # Adjusted circle radius

    # Create the left curve
    turtle.left(120)
    turtle.circle(-56, 200)  # Adjusted circle radius

    # Complete the shape
    turtle.forward(112)  # Adjusted forward movement
    turtle.end_fill()

def draw_allah_name():
    # List of colors for the name (adding 10 new colors)
    colors = [
        "red", "orange", "yellow", "green", "blue", 
        "indigo", "violet", "pink", "purple", "cyan", 
        "magenta", "gold", "silver", "lime", "teal", 
        "coral", "navy", "brown", "crimson", "khaki"
    ]
    
    # Complement colors for the hearts
    heart_colors = [
        "green", "blue", "purple", "red", "orange"
    ]

    # Draw 5 hearts
    for i in range(5):
        # Calculate x position for hearts
        x_position = -50 + (i * 25)  # Adjust spacing for hearts
        draw_heart(x_position, -50, heart_colors[i % len(heart_colors)])

    # Write "اللہ" in the center of the hearts
    turtle.penup()
    turtle.goto(0, -40)  # Center position for the text
    turtle.pendown()

    # Animate the text with a bounce effect
    for j in range(10):
        turtle.color(random.choice(colors))  # Random color for each name
        turtle.clear()  # Clear the previous text
        turtle.goto(0, -40 + (j % 2) * 10)  # Bounce effect
        turtle.write("اللہ", font=("Arial", 50, "bold"), align="center")

# Set the turtle speed
turtle.speed(1)

# Set background color for better visibility
turtle.bgcolor("black")

# Draw the name "اللہ" and heart shape
draw_allah_name()

# Finish the drawing
turtle.hideturtle()  # Hide the turtle cursor
turtle.done()
