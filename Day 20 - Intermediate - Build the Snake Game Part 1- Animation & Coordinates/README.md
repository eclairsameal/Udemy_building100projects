# Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates

## Step 1 - Create a snake body

## Step 2 - Move the snake

### 畫面的更新

* turtle.tracer(n=None, delay=None)

Turn turtle animation on/off and set delay for update drawings. If n is given, only each n-th regular screen update is really performed. (Can be used to accelerate the drawing of complex graphics.)

打開/關閉海龜動畫並設置更新圖紙的延遲。 如果給定 n，則僅真正執行第 n 次常規屏幕更新。 （可用於加速復雜圖形的繪製。）

* turtle.update()

Perform a TurtleScreen update. To be used when tracer is turned off.

執行 TurtleScreen 更新。 在跟踪器關閉時使用。

### 移動

只用forward()控制向前，當蛇頭向上移動時，後面的部分會繼續前進

```python
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    for body in body_list:
        body.forward(20)
    body_list[0].left(90)
```

![](https://i.imgur.com/fgLI1FD.gif)

後一項移動到前一項的位置

```python
while game_is_on:
    screen.update()
    time.sleep(0.5)

    for body_num in range(len(body_list) - 1, 0, -1):
        new_x = body_list[body_num - 1].xcor()
        new_y = body_list[body_num - 1].ycor()
        body_list[body_num].goto(new_x, new_y)
    body_list[0].forward(20)
    body_list[0].left(90)
```

![](https://i.imgur.com/oM7fiwV.gif)

## Step 2.5 - Create a Snake Class & Move to OOP

* Snake
* main




