# Intermediate+ Stock Trading News Alert Project

追蹤浮動過大股票相關新聞的系統(寄SNS)

## STEP 1: Use [ALPHA VANTAGE](https://www.alphavantage.co/)

When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

### TIME_SERIES_DAILY_ADJUSTED

此 API 返回指定全球股票的原始（交易時）每日開盤/高/低/收盤/成交量值、每日調整後的收盤值和歷史拆分/股息事件，涵蓋 20 多年的歷史數據。

```python
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
```

## STEP 2: Use [News Api](https://newsapi.org/)

Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

```python
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEW_API_KEY,
}
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
```

## STEP 3: Use [twilio](https://www.twilio.com/try-twilio)

```python
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in articles_3:
    message = client.messages.create(
        body=article,
        from_=VIRTUAL_TWILIO_NUMBER,
        to=VERIFIED_NUMBER
    )
```