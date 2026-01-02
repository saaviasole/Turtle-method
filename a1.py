import turtle

# Creating Screen
screen = turtle.screen()
screen.setup(width=650, hight=650)
screen.bgcolor("aqua")
screen.title("Drawing a square")

# Create Turtle
pen = turtle.Turtle()
pen.color("black")
pen.pensize(3)

# Draw a square
for i in range(4):
    pen.forward(100)
    pen.right(90)

    # keep thw window open
    turtle.done
