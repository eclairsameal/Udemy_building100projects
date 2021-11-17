# Day 21 - Intermediate - Build the Snake Game Part 2 - Inheritance & List Slicing

[Class-Inheritance](https://replit.com/@appbrewery/Class-Inheritance)

## Snake Game Part 2

* Detect collision with food

* Create a Scoreboard

* Detect collision with wall

* Detect collision with tail

### Scoreboard.class

```python
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 20, "normal"))
```

將重複的 code 函數化

```python
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
```

將一些變數常數化

```python
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
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FORT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
```