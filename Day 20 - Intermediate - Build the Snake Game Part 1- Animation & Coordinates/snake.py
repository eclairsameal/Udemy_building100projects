from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTION = [0, 90, 180, 270]


class Snake:
    def __init__(self):
        self.body_list = []
        self.create_snake()
        self.head = self.body_list[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            new_body = Turtle(shape="square")
            new_body.color("white")
            new_body.penup()
            new_body.goto(positions)
            self.body_list.append(new_body)

    def move(self):
        for body_num in range(len(self.body_list) - 1, 0, -1):
            new_x = self.body_list[body_num - 1].xcor()
            new_y = self.body_list[body_num - 1].ycor()
            self.body_list[body_num].goto(new_x, new_y)
        self.body_list[0].forward(MOVE_DISTANCE)

    def up(self):
        self.body_list[0].setheading(90)

    def down(self):
        self.body_list[0].setheading(270)

    def left(self):
        self.body_list[0].setheading(180)

    def right(self):
        self.body_list[0].setheading(0)
