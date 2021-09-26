from turtle import Turtle

ALIGNMENT = "center"
FORT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FORT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FORT)