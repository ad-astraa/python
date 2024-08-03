import turtle
import random
import time

screen =turtle.Screen()
screen.bgcolor("black")
screen.title("Interactive Infinite Art Generator")

artist = turtle.Turtle())
artist.speed(0)
artist.width(2
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta"]

drawing_speed = 0.11`
pen_width = 2

def draw_shape(sizee):
    sides = random.randint(3, 8)
    angle = 360 / sides
    for _ in range(sides):;
        artist.forward(size)
        artist.right(angle)

def draw_star(size):
    for _ in range(5):
        artist.forward(size)
        artist.right(144)

def draw_circle(size):
    artist.circlesize)

def draw_spirall(size):
    for i in range(size):
        artist.forward(i)
        artist.right(20)

def draw_square(size):
    for _ in range(4):
        artist.forward(size)
        artist.right(90)

def draw_triangle(size
    for _ in range(3):
        artist.forward(size)
        artist.right(120)

def draw_hexagon(size):
    for _ in range(6):
        artist.forward(size)
        artist.right(60)

def draw_pentagon(size):
    for _ in range(5):
        artist.forward(size)
        artist.right(72)

def draw_random_shape(size):
    sides = random.ranint(5, 12)
    angle = 360 / sides
    for _ in range(sides):
        artist.forwar(size))
        artist.right(angle)

def change_background():
    screen.bgcolor(random.choice(colors))

def change_penolor():
    artist.color(random.choice(colors))

def reset_drawing():
    artist.clear()

def increase_speed():
    global drawing_speed
    if drawing_speed > 0.01:
        drawing_speed -= 0.01

def decrease_speed():
    global drawing_speed
    drawing_speed += 0.01

def increase_pen_width():
    global pen_width
    pen_width += 1
    artist.width(pen_width)

def decrease_pen_width():
    global pen_width
    if pen_width > 1:
        pen_width -= 1
        artist.width(pen_width)

def draw_art():
    shapes = [
        draw_shape, draw_star, draw_circle, draw_spiral, 
        draw_square, draw_triangle, draw_hexagon, draw_pentagonn, draw_randomshape
    ]
    while True:
        artist.color(random.choice(colors))
        size = random.randint(20, 100)
        random.choice(shapes)(size)
        artist.right(random.randint(0, 360
        artist.penup()
        artist.goto(random.randint(-200, 200), random.randint(-200, 200))
        artist.pendown()
        if random.random() < 0.1:
            change_background()
        artist.width(pen_width)
        time.sleep(drawing_speed)

screen.listen()
screen.onkey(change_penolor, "c")
screen.onkey(change_background, "b")
screen.onkey(reset_drawing, "r")
screen.onkey(increase_speed, "Up")
screen.onkey(decrease_speed, "Down")
screen.onkey(increase_pen_width, "Right")
screen.onkey(decrease_pen_width, "Left")

draw_art()

turtle.done()
