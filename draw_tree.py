import turtle
import random

def draw_tree(branch_len, t):
    if branch_len > 5:  # Limit the branch length for recursion
        # Draw the main branch
        t.forward(branch_len)

        # Draw the right subtree
        t.right(20)  # Angle for right branch
        draw_tree(branch_len - 15, t)  # Decrease the length for the next branch

        # Draw the left subtree
        t.left(40)  # Angle for left branch
        draw_tree(branch_len - 15, t)  # Decrease the length for the next branch

        # Return to the original branch
        t.right(20)  # Return to original angle
        t.backward(branch_len)  # Move back to the original position
    else:
        # Draw leaves at the end of branches
        draw_leaves(t)

def draw_flower(t):
    # Draw a flower at the current position
    t.color(random.choice(["red", "pink", "yellow", "purple", "blue"]))
    t.begin_fill()
    t.circle(5)  # Flower center
    t.end_fill()
    t.penup()
    t.backward(5)  # Move back to the branch
    t.pendown()

def draw_leaves(t):
    # Draw leaves at the end of branches
    t.color("green")
    t.begin_fill()
    t.circle(5)  # Leaf size
    t.end_fill()
    t.penup()
    t.backward(5)  # Move back to the branch
    t.pendown()

def draw():
    # Set up the turtle
    turtle.bgcolor("skyblue")  # Background color
    turtle.speed(0)  # Fastest drawing
    turtle.pensize(2)  # Set the pen size
    turtle.color("brown")  # Trunk color

    # Position the turtle to start drawing
    turtle.left(90)  # Point the turtle upwards
    turtle.up()  # Lift the pen
    turtle.backward(100)  # Move back to position the tree better
    turtle.down()  # Lower the pen

    # Draw the tree
    draw_tree(100, turtle)  # Initial branch length

    # Draw random flowers at random positions
    for _ in range(5):  # Draw 5 flowers
        turtle.penup()
        x = random.randint(-200, 200)
        y = random.randint(0, 200)
        turtle.goto(x, y)
        turtle.pendown()
        draw_flower(turtle)

    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

# Run the drawing function
draw()
