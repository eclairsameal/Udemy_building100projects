import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
response.raise_for_status()  # 根據回傳的結果引發 HTTP 錯誤
data = response.json()
# print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)