# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockkwise
# C = Clear drawing

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def clear_drawing():
    turtle.clear()
    turtle.up()
    turtle.home()
    turtle.down()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()

