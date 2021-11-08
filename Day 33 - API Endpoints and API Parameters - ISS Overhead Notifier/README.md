# Day 33 - API Endpoints & API Parameters - ISS Overhead Notifier

Endpoints: 端點

追蹤國際空間站(利用API)當到上空時，寄信通知自己。

[International Space Station(國際太空站)wiki](https://en.wikipedia.org/wiki/International_Space_Station)

## API

[Application Programming Interface wiki](https://en.wikipedia.org/wiki/API)

[google JSON Viewer 外掛](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh)

[International Space Station Current Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
```

**Result**

```python
<Response [200]>
```

[HTTP Status Codes](https://httpstatuses.com/)

[Requests: HTTP for Humans](https://docs.python-requests.org/en/latest/)

[Reverse() Geocoding Convert Lat Long to Address(反向地理編碼將經緯度轉換為地址)](https://www.latlong.net/Show-Latitude-Longitude.html)

## Kanye West quotes

[kanye.rest](https://kanye.rest/)

##

[Sunset and sunrise times API](https://sunrise-sunset.org/api)