import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turtle.pensize(10)
turtle.speed('fastest')

for i in range(200):
    turtle.forward(30)
    turtle.color(random_color())
    #turtle.color(random.choice(colours))
    # turtle.right(random.choice(directions))
    turtle.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
