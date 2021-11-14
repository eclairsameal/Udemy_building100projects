# Day 29 - Building a Password Manager GUI App with Tkinter

[color hunt](https://colorhunt.co/)

[tk docs](https://tkdocs.com/tutorial/canvas.html#creating)

## columnspan 合併欄位

[grid-columnspan-demo](https://replit.com/@appbrewery/grid-columnspan-demo#main.py)

![](https://i.imgur.com/2BuzjO1.png)

```python
from tkinter import *

window = Tk()

r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2)


window.mainloop()
```

## Pyperclip

一個跨平台的 Python 模塊，用於復制和粘貼剪貼板功能

[pyperclip](https://pypi.org/project/pyperclip/)

