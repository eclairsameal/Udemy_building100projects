from turtle import Turtle

ALIGNMENT = "center"
FORT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        #self.write(f"Score: {self.score} ", align="center", font=("Arial", 20, "normal"))
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FORT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
