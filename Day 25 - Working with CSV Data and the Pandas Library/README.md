# Day 25 - Intermediate - Working with CSV Data and the Pandas Library

[API reference](https://pandas.pydata.org/docs/reference/index.html)

[pandas documentation](https://pandas.pydata.org/docs/)


## U.S. States Game

turtle 只適用gif的圖像格式

### 取得圖上的座標

```
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
# Get the coordinates of the mouse click (得到滑鼠按下的座標)
turtle.mainloop() 

# screen.exitonclick() # The program will exit after clicking the mouse(按下滑鼠後會結束程式)
```

### Target

1. Convert(轉換) the guess to Title case
2. Check if the guess is among the 50 states
3. Write correct guesses onto the map
4. Use a loop to allow the user to keep guessing
5. Record the correct guesses in a list
6. Keep track of the score