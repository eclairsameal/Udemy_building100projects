import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "                      "
TOKEN = "                       "
GRAPH_ID = "graph1"

""" 成功創立帳號後，就不用再執行
# post users 要求的參數dict
user_params = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(pixela_endpoint, json=user_params) 
print(response.text)
"""

# ----------- 建立圖 -----------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "int",
    "color": "kuro",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ----------- 填入一個 pixel -----------
# POST - /v1/users/<username>/graphs/<graphID>
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()  # 2021-11-22 06:11:06.051933
# today = datetime(year=2021, month=11, day=21)
# print(today.strftime("%Y%m%d")) # 20211121
post_pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("coding: "),
 }
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
# print(response.text)

# ----------- 修改 pixel -----------
today = datetime(year=2021, month=11, day=21).strftime("%Y%m%d")
# PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_pixel = {
    "quantity": "6",
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=headers)
# print(response.text)

# ----------- 刪除 pixel -----------
today = datetime(year=2021, month=11, day=21).strftime("%Y%m%d")
# DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.delete(url=delete_pixel_endpoint,  headers=headers)
# print(response.text)

