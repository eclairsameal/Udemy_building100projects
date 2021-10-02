from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class CheckStates(Turtle):
    def __init__(self):
        super().__init__()
        self.correct = 0
        self.data = pandas.read_csv("50_states.csv")
        self.all_states = self.data.state.to_list()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.guessed_states = []

    def check_answer(self, ans):
        correct_state = self.data[self.data["state"] == ans]
        if not correct_state.empty:
            print(correct_state)
            self.correct += 1
            self.goto(int(correct_state["x"]), int(correct_state["y"]))
            self.write(ans, align="left", font=FONT)
            self.guessed_states.append(ans)
            #self.write(correct_state.state.item(), align="left", font=FONT)

    def output_missing_states(self):
        missing_states = []
        for state in self.all_states:
            if state not in self.guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
