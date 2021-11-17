from turtle import Turtle, Screen
import time

# Move the snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
body_list = []

for positions in starting_positions:
    new_body = Turtle(shape="square")
    new_body.color("white")
    new_body.penup()
    new_body.goto(positions)
    body_list .append(new_body)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    for body_num in range(len(body_list) - 1, 0, -1):
        new_x = body_list[body_num - 1].xcor()
        new_y = body_list[body_num - 1].ycor()
        body_list[body_num].goto(new_x, new_y)
    body_list[0].forward(20)
    #body_list[0].left(90)





screen.exitonclick()
