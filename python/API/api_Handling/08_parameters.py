
# Your API does not support query parameters, but here's how they are used:

import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

params = {
    "page": 1,
    "limit": 10
}

response = requests.get(url, params=params)

print(response.url)
print(response.status_code)