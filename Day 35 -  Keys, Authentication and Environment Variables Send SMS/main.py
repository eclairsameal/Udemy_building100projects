import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "天氣的api key"

account_sid = ""
auth_token = ""

parameters = {
    "lat": 35.689487,
    "lon": 139.691711,
    "appid": api_key,
    "exclude": "current,minutely,daily"  # 排除某些資料
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]['weather'][0]['id'])  # ['weather']是list所以要用[0]取值
weather_data_12h = weather_data["hourly"][:12]

will_rain = False

for h in weather_data_12h:
    # print(h['weather'][0]['id'])
    condition_code = h['weather'][0]['id']
    if condition_code < 700:
        # print("Bring an umbrella.")
        will_rain = True
        break

if will_rain:
    # print("Bring an umbrella.")

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+13802071751',
        to='+817043277580'
    )
    print(message.sid)