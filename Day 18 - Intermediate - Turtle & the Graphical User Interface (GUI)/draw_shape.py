import turtle as t
import random

turtle = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(sides, tu):
    for _ in range(sides):
        tu.forward(100)
        tu.right(360 / sides)


for i in range(3, 11):
    turtle.color(random.choice(colours))
    draw_shape(i, turtle)

screen = t.Screen()
screen.exitonclick()
