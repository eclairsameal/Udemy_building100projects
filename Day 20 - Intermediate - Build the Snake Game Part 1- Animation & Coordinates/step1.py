from turtle import Turtle, Screen

# Create a snake body

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for positions in starting_positions:
    new_body = Turtle(shape="square")
    new_body.color("white")
    new_body.goto(positions)

screen.exitonclick()
