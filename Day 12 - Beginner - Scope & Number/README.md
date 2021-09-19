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
