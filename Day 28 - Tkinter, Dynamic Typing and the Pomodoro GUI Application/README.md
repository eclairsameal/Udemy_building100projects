# Day 28 - Tkinter, Dynamic Typing and the Pomodoro GUI Application

## Pomodoro

```
25min Work
5min Break
25min Work
5min Break
25min Work
5min Break
25min Work
20min Break
```

## Event Driven

### tk.after(ms, function_name, *parameter)

過了特定毫秒後執行此function

```python
def say_something(a, b, c):
    print(a)
    print(b)
    print(c)
    
window.after(1000, say_something, 283, 765, 39)
```