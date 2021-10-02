from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class CheckStates(Turtle):
    def __init__(self):
        super().__init__()
        self.correct = 0
        self.data = pandas.read_csv("50_states.csv")
        self.color("black")
        self.penup()
        self.hideturtle()

    def check_answer(self, ans):
        correct_state = self.data[self.data["state"] == ans]
        if not correct_state.empty:
            print(correct_state)
            self.correct += 1
            self.goto(int(correct_state["x"]), int(correct_state["y"]))
            self.write(ans, align="left", font=FONT)
            #self.write(correct_state.state.item(), align="left", font=FONT)