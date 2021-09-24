import turtle as t

turtle = t.Turtle()

for _ in range(15):
    turtle.forward(10)
    turtle.up()
    turtle.forward(10)
    turtle.down()

screen = t.Screen()
screen.exitonclick()