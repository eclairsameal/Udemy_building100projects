from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Close animation

paddle = Turtle(shape="square")
paddle.penup()
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(350, new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(350, new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()


