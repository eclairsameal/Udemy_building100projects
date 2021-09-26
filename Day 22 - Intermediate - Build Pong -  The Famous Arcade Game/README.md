# Day 22 - Intermediate - Build Pong : The Famous Arcade Game

## Breakdown the Problem

Create the screen

Create and move a paddle

Create another paddle

Create the ball and make it move

Detect collision with wall and bounce

Detect collision with paddle

Detect when paddle misses

Keep score

## Create the screen

width=800

height=600

## Create and move a paddle

paddle:
```
    width = 20
    height = 100
    x_pos = 350
    y_pos = 0
    move = +-20
```

### animation
```python
import time
screen.tracer(0)  # Close animation
    .
    .
    .
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
```
    