# Day 32 - Send Email (smtplib) & Manage Dates (datetime)

## SMTP

Simple Mail Transfer Protocol

[smtplib — doc](https://docs.python.org/3/library/smtplib.html)


### SMTP Information

|          | Gmail | Hotmail | Yahoo |
| -------- | -------- | -------- | -------- |
| host     | smtp.gmail.com | smtp.live.com | smtp.mail.yahoo.com |

* .starttls()

Put the SMTP connection in TLS mode

TLS(Transport Layer Security) : 保護email服務的一種方式，能確保連接的安全。

* .login(user=, password=)

Log in on an SMTP server that requires authentication(驗證).

* .connection.sendmail(from_addr, to_addrs, msg)

    * from_addr: 寄件者

    * to_addrs: 收件者

    * msg: "Subject:主題\n\n內容"

::: danger

* TimeoutError:  

Add a port number by changing your code to this:

smtplib.SMTP("smtp.gmail.com", port=587)

* unicodeencodeerror: 'ascii' codec can't encode characters in position 5-6: ordinal not in range(128)

電腦名稱不是英文導致錯誤..... 

:::

## Datetime

[datetime - doc](https://docs.python.org/3/library/datetime.html)

## Challenge 1 - Send Motivational Quotes on Mondays via Email

偵伺今天是否是星期一，是的話寄一句話到信箱

## 託管並定時運行code

Host, run, and code Python in the cloud!

https://www.pythonanywhere.com/
