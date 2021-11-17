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

http://tcl.tk/man/tcl8.6/TclCmd/after.htm

過了特定毫秒後執行此function

```python
def say_something(a, b, c):
    print(a)
    print(b)
    print(c)
    
window.after(1000, say_something, 283, 765, 39)
```

## Dynamic Typing

通過變數改變變數型態

[Is Python strongly typed?](https://stackoverflow.com/questions/11328920/is-python-strongly-typed)