import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(color, width, height, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_boy():
    # Head
    draw_circle("blue", 30, -100, 70)  # Boy's head
    # Body
    draw_rectangle("lightblue", 60, 80, -130, -10)  # Boy's body
    # Arms
    draw_rectangle("lightblue", 15, 60, -145, -10)  # Left arm
    draw_rectangle("lightblue", 15, 60, -55, -10)  # Right arm
    # Legs
    draw_rectangle("blue", 20, 60, -130, -90)  # Left leg
    draw_rectangle("blue", 20, 60, -70, -90)  # Right leg

def draw_girl():
    # Head
    draw_circle("pink", 30, 100, 70)  # Girl's head
    # Body
    draw_rectangle("lightpink", 60, 80, 70, -10)  # Girl's body
    # Arms
    draw_rectangle("lightpink", 15, 60, 55, -10)  # Left arm
    draw_rectangle("lightpink", 15, 60, 145, -10)  # Right arm
    # Legs
    draw_rectangle("pink", 20, 60, 70, -90)  # Left leg
    draw_rectangle("pink", 20, 60, 130, -90)  # Right leg

def draw_flower(x, y):
    # Flower petals
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    
    for color in colors:
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(15, 60)  # Petal size
        turtle.left(120)
        turtle.circle(15, 60)
        turtle.left(120)
        turtle.end_fill()
        turtle.right(60)  # Rotate for next petal

    # Flower center
    draw_circle("yellow", 10, x, y - 10)

def draw_scene():
    turtle.speed(2)  # Moderate speed
    turtle.bgcolor("lightgreen")  # Background color

    # Draw boy and girl
    draw_boy()
    draw_girl()

    # Draw flower given by boy to girl
    draw_flower(-100, -20)  # Flower near boy
    draw_flower(100, -20)  # Flower near girl

    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

# Run the drawing function
draw_scene()
