
# This API doesn't require authentication.

import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

response = requests.get(url, headers=headers)

print(response.status_code)