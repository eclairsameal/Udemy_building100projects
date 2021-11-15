# Day 34 - Intermediate+ API Practice - Creating a GUI Quiz App

Day 17 有寫過文字版的問答遊戲，Day 34 的目標是利用api跟tkinter來對舊專案進行升級，讓問答遊戲介面化，並且題目每次都不一樣。

![](https://i.imgur.com/Xsr89Zk.png)

## 利用API來替換data.py裡的值

[Question database](https://opentdb.com/)

**API URL GENERATED:**

```
https://opentdb.com/api.php?amount=10&type=boolean
```

```python
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
```

## 題目亂碼

在HTML當中有些符號會用一些特殊編碼來代表

[HTML Entities](https://www.w3schools.com/html/html_entities.asp)

**轉換編碼的網站**

[FREEFORMATTER.COM](https://www.freeformatter.com/html-escape.html)


**Solution**

```python
import html
print(html.unescape('&pound;682m'))
```

[Decode HTML entities in Python string?](https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string)

## UI Class

* 設定寬，文字超出會換行
* 
* canvas 的 padding 在grid裡設定

```python
self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,  # 設定寬，文字超出會換行
            text="question_text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
```

將Class 傳到另一個 Class中

```python
# main
quiz_ui = QuizInterface(quiz)  # 將建立的問題集傳給ui

# ui
from quiz_brain import QuizBrain # 當在QuizInterface編輯程式時，可以有QuizBrain提示
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # 先宣告傳入的資料是什麼型態，避免犯錯
    ...

```

## 指定資料型態(Type Hints)

```python
age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")
```
