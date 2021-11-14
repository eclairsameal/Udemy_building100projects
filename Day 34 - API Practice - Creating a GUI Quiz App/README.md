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