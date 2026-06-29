import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

try:
    response = requests.get(url, timeout=5)

    print(response.status_code)

except requests.exceptions.Timeout:
    print("Request Timed Out")