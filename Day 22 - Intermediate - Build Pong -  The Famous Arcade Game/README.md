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

 ## Create another paddle

將 paddle class 化

## Detect collision with wall and bounce

球超越上邊界跟下邊界時反彈

反彈:將移動量*(-1)

球有大小所以要預留空間

## Detect collision with paddle

直覺: ball.distance(r_paddle) < 20 -> 判斷為碰撞，但ball.distance(r_paddle)是算中心點之間的距離，所以邊緣的碰撞的話，ball.distance(r_paddle) 會大於20。

* 修改判斷: 當球經過 x 的某一點，並且距離在50以內，也算碰撞。

* 340 -> 320 讓反彈更自然

```
ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320
```