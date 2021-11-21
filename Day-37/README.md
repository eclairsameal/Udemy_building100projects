# Day 37 - Intermediate+ Habit Tracking Project: API Post Requests & Headers

[pixela](https://pixe.la/)

[Developer Interface](https://docs.python-requests.org/en/latest/api/)

[Datetime用法](https://www.w3schools.com/python/python_datetime.asp)


## HTTP Requests

* GET

向外部系統索取一個特定的數據，他們在回復中給我們。

```python
requests.get()
```

* POST

我們給外部系統一些數據的地方。而我們除了對我們得到的回應不感興趣外，對其他的回應也不感興趣，無論是否成功。

```python
requests.post()
```

* PUT

更新資料

```python
requests.put()
```

* DELETE

刪除

```python
requests.delete()
```

## pixela

[Pixela API Document](https://docs.pixe.la/)

### [Create a user](https://docs.pixe.la/entry/post-user)

在pixela建立帳號(Create a new Pixela user)

```python
# POST - /v1/users
pixela_endpoint = "https://pixe.la/v1/users"

# post 要求的參數dict
user_params = {
    "token": "Validation rule: [ -~]{8,128}",
    "username": "Validation rule: [a-z][a-z0-9-]{1,32}",
    "agreeTermsOfService": "yes",  # 是否同意條款
    "notMinor": "yes",  # 是否為成人
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.text)
```

**成功**

```
{"message":"Success. Let's visit https://pixe.la/@sisyphean , it is your profile page!","isSuccess":true}
```

###  [Create a graph](https://docs.pixe.la/entry/post-graph)

Create a new pixelation graph definition.

```python
# POST - /v1/users/<username>/graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "int",
    "color": "kuro",
}

response = requests.post(url=graph_endpoint, json=graph_config)
print(response.text)
```

直接執行會出現找不到User的回報，那是因為我們沒也傳username跟token。

```
{"message":"User `sisyphean` does not exist or the token is wrong.","isSuccess":false}
```

## Headers - 更安全傳送要求的方法

之前的get要求都是將key或token直接寫在url，所有秘密的東西都在請求本身。所以如果有人在監視這個，他們將能夠看到所有的資料，也夠竊取API密鑰。 其中一件讓人放心的事情是，這個API是通過HTTPS和。 S代表安全的意思。所以這個請求其實是加密的。但這並不妨礙有人在你的瀏覽器上安裝一些東西來尋找API密鑰。所以對於一些API提供者來說。看希望使用者在Headers中提供認證。

```python
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# {"message":"Success.","isSuccess":true}
```

**查看建立的圖**

```
https://pixe.la/v1/users/sisyphean/graphs/graph1.html
```

###  [Post a pixel](https://docs.pixe.la/entry/post-pixel)

It records the quantity of the specified date as a "Pixel".

```python
# POST - /v1/users/<username>/graphs/<graphID>
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_pixel_data = {
    "date": "20211122",
    "quantity": "4",
 }
response = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
print(response.text)
```

