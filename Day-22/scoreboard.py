from turtle import Turtle

ALIGNMENT = "center"
FORT = ("Courier", 70, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FORT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FORT)

    def l_get_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_get_point(self):
        self.r_score += 1
        self.update_scoreboard()
