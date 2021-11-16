# Day 35 - Intermediate+ Keys, Authentication & Environment Variables: Send SMS

建立下雨提醒系統

[OpenWeather](https://openweathermap.org/)

創帳號以便取得API Key

[Latlong.net(查詢經緯)](https://www.latlong.net/)

[Online JSON View](http://jsonviewer.stack.hu/)

## API Authentication

能更安全的訪問已獲取更有價值數據，API 提供方會利用API Key來驗證或追蹤使用者利用API的狀況。

[Current(當前) weather data](https://openweathermap.org/current)

Call current weather data for one location - By city name

```
api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
q = Tokyo,JP
Latitude = 35.689487
Longitude = 139.691711
```

## 測試

抓取東京的天氣資料

[One Call API](https://openweathermap.org/api/one-call-api)

```
https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
Latitude = 35.689487
Longitude = 139.691711
```

```python
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""

parameters = {
    "lat": 35.689487,
    "lon": 139.691711,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
```

## 暴雨提醒系統(文字顯示)

每天早上7:00檢查未來12小時內會下雨嗎?

**善用API的文件**

* 此API有一個exclude參數可以排除我們不感興趣的資料。

```
parameters = {
    "lat": 35.689487,
    "lon": 139.691711,
    "appid": api_key,
    "exclude": "current,minutely,daily"  # 排除某些資料
}
```

* 文件裡有天氣編碼(id)相關的表 - [Weather Conditions codes](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)

```
if id < 7000: 可能要帶傘(Bring an umbrella.)
```

[ventusky(世界天氣)](https://www.ventusky.com/)找會下雨的地方，方便測試。

```python
# print(weather_data["hourly"][0]['weather'][0]['id'])  # ['weather']是list所以要用[0]取值
weather_data_12h = weather_data["hourly"][:12]
for h in weather_data_12h:
    # print(h['weather'][0]['id'])
    condition_code = h['weather'][0]['id']
    if condition_code < 700:
        print("Bring an umbrella.")
        break
```

## Sending SMS (twilio API)

[twilio](https://www.twilio.com/try-twilio)

[quickstart](https://www.twilio.com/docs/sms/quickstart/python)

## 託管並定時運行code

Host, run, and code Python in the cloud!

https://www.pythonanywhere.com/

使用pythonanywhere免費版會出現錯誤，請用下面的說明修復程式

[How to get Twilio to work on Free accounts with the proxy](https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/)

## Environment Variable

[wiki](https://en.wikipedia.org/wiki/Environment_variable)

* Convenience(方便): 不修改程式碼下方便修改變數
* Security(安全): 讓敏感資訊跟程式碼區隔開來
