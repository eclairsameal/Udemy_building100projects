import turtle as t
import random

turtle = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turtle.pensize(10)
turtle.speed('fastest')

for i in range(200):
    turtle.forward(30)
    turtle.color(random.choice(colours))
    # turtle.right(random.choice(directions))
    turtle.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
