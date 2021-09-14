# day8-Beginner-Function Parameters and Caesar Cipher

## day-8-1-exercise

[Area Calc](https://replit.com/@appbrewery/day-8-start)

## day-8-2-exercise

[Prime Numbers](https://replit.com/@appbrewery/day-8-2-exercise)

## Caesar Cipher(凱撒密碼)

[wiki](https://zh.wikipedia.org/wiki/%E5%87%B1%E6%92%92%E5%AF%86%E7%A2%BC)

### caesar-cipher-1

Encryption

[caesar-cipher-1-start](https://replit.com/@appbrewery/caesar-cipher-1-start)

```
Type 'encode' to encrypt, type 'decode' to decrypt:
g
Type your message:
civilization
Type the shift number:
5
The encoded text is: hnanqnefynts
```

🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

'civilization' 中有 z 直接加 shift 的值會超出 list 的範圍

### caesar-cipher-2

Decrypt

[caesar-cipher-2-start](https://replit.com/@appbrewery/caesar-cipher-2-start)

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
helloaz
Type the shift number:
5
The encoded text is: mjqqtfe

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqtfe
Type the shift number:
5
The encoded text is helloaz
```

### caesar-cipher-3

優化程式碼

[caesar-cipher-3-start](https://replit.com/@appbrewery/caesar-cipher-3-start)

### caesar-cipher-4

提高使用者體驗 and 防呆

[caesar-cipher-4-start](https://replit.com/@appbrewery/caesar-cipher-4-start)

```
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
helloaz 5
Type the shift number:
5
Here's the encoded result: mjqqtfe 5
Type 'yes' if you want to go again. Otherwise type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqtfe 5
Type the shift number:
5
Here's the decoded result: helloaz 5
Type 'yes' if you want to go again. Otherwise type 'no'.
no
Goodbye
```
