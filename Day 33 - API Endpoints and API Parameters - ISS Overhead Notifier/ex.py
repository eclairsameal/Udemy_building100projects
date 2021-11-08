import requests

MY_LAT = 51.507351
MY_LONG = -0.127758

"""
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
response.raise_for_status()  # 根據回傳的結果引發 HTTP 錯誤
data = response.json()
# print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
"""
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise, sunset)