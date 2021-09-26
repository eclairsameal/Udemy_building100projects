from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # 增加限制讓蛇不能回頭
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
