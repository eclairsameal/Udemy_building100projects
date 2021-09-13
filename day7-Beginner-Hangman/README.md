# Hangman

[wiki](https://en.wikipedia.org/wiki/Hangman_(game))

[web](https://hangmanwordgame.com/?fca=1&success=0#/)

![](https://i.imgur.com/RojI5hR.png)


## code

### Step 1 

亂數在list中選一個單字(chosen_word)

個別判斷chosen_word的字母跟使用者輸入的字母有符合嗎

![](https://i.imgur.com/bym4hjz.png)

### Step 2

將判斷以 ```["_", "_", "_", "_", "_"]``` 的方式表示

![](https://i.imgur.com/OdNaIat.png)

### Step 3

完成直到猜對所有字母的while遊戲循環

![](https://i.imgur.com/QjdeNg3.png)

### Step 4
加上上吊人的機制(輸的判定)跟畫出上吊人的 ASCII art

![](https://i.imgur.com/WrAstVQ.png)

### Step 5
* 完善使用者體驗
* 將單字跟ASCII art拆成模組