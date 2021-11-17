# Day 12 - Beginner - Scope & Number

## Modifying Global Scope

不要修改修改全域變數，如果修改全域變數，請用 function return。

```python=
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

    enemies = increase_enemies()
    print(f"enemies outside function: {enemies}")
```

## [ASCII art](http://patorjk.com/software/taag/#p=display&f=Slant&t=Number%20Guessing)

## Number Guessing Game

[guess-the-number-start](https://replit.com/@appbrewery/day-12-start#main.py)

[guess-the-number-final](https://replit.com/@appbrewery/guess-the-number-final#main.py)
